/* C97 persistent zran adapter.  This file deliberately serializes fields,
 * never a host C structure.  The enclosing Python boundary authenticates the
 * scientific source and fills the fixed hash slots after this writer closes. */
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

#include "zran.h"

#define HEADER_BYTES 280U
/* out, in, bit count, member/flags byte, dictionary length, dictionary */
#define RECORD_BYTES (8U + 8U + 1U + 1U + 4U + 32768U)
static const unsigned char magic[8] = {'C','9','7','Z','R','A','I','1'};

static int put_u32(FILE *out, uint32_t value) {
    unsigned char b[4] = {(unsigned char)(value >> 24), (unsigned char)(value >> 16),
                          (unsigned char)(value >> 8), (unsigned char)value};
    return fwrite(b, 1, 4, out) == 4 ? 0 : -1;
}
static int put_u64(FILE *out, uint64_t value) {
    unsigned char b[8]; int n;
    for (n = 7; n >= 0; n--) { b[n] = (unsigned char)value; value >>= 8; }
    return fwrite(b, 1, 8, out) == 8 ? 0 : -1;
}
static int get_u32(FILE *in, uint32_t *value) {
    unsigned char b[4]; if (fread(b, 1, 4, in) != 4) return -1;
    *value = ((uint32_t)b[0] << 24) | ((uint32_t)b[1] << 16) | ((uint32_t)b[2] << 8) | b[3]; return 0;
}
static int get_u64(FILE *in, uint64_t *value) {
    unsigned char b[8]; int n; if (fread(b, 1, 8, in) != 8) return -1; *value = 0;
    for (n = 0; n < 8; n++) *value = (*value << 8) | b[n]; return 0;
}
static int write_header(FILE *out, const struct deflate_index *index, uint64_t bytes, uint64_t span) {
    unsigned char zero[224] = {0};
    if (fwrite(magic, 1, 8, out) != 8 || put_u32(out, 1) || put_u32(out, 0x01020304) ||
        put_u32(out, (uint32_t)index->mode) || put_u32(out, RECORD_BYTES) ||
        put_u64(out, bytes) || put_u64(out, (uint64_t)index->length) || put_u64(out, span) ||
        put_u64(out, (uint64_t)index->have) || fwrite(zero, 1, sizeof(zero), out) != sizeof(zero)) return -1;
    return 0;
}
static int write_index(FILE *out, const struct deflate_index *index, uint64_t bytes, uint64_t span) {
    int i; if (write_header(out, index, bytes, span)) return -1;
    for (i = 0; i < index->have; i++) {
        point_t *p = index->list + i;
        if (put_u64(out, (uint64_t)p->out) || put_u64(out, (uint64_t)p->in) ||
            fputc(p->bits, out) == EOF || fputc(0, out) == EOF || put_u32(out, 32768) ||
            fwrite(p->window, 1, 32768, out) != 32768) return -1;
    }
    return fflush(out) == 0 ? 0 : -1;
}
static struct deflate_index *read_index(FILE *in) {
    unsigned char got[8], discard[224]; uint32_t version, endian, mode, recsize, dictionary; uint64_t source, length, span, count; int i;
    struct deflate_index *index;
    if (fread(got, 1, 8, in) != 8 || memcmp(got, magic, 8) || get_u32(in, &version) || get_u32(in, &endian) ||
        get_u32(in, &mode) || get_u32(in, &recsize) || get_u64(in, &source) || get_u64(in, &length) ||
        get_u64(in, &span) || get_u64(in, &count) || fread(discard, 1, 224, in) != 224 ||
        version != 1 || endian != 0x01020304 || recsize != RECORD_BYTES || count == 0 || count > INT32_MAX) return NULL;
    index = calloc(1, sizeof(*index)); if (index == NULL) return NULL;
    index->list = calloc((size_t)count, sizeof(point_t)); if (index->list == NULL) { free(index); return NULL; }
    index->have = (int)count; index->mode = (int)mode; index->length = (off_t)length;
    for (i = 0; i < index->have; i++) {
        uint64_t out, compressed; int bits, member;
        if (get_u64(in, &out) || get_u64(in, &compressed) || (bits = fgetc(in)) == EOF || (member = fgetc(in)) == EOF ||
            get_u32(in, &dictionary) || member != 0 || dictionary != 32768 || bits < 0 || bits > 7 ||
            fread(index->list[i].window, 1, 32768, in) != 32768) { deflate_index_free(index); return NULL; }
        index->list[i].out = (off_t)out; index->list[i].in = (off_t)compressed; index->list[i].bits = bits;
        if ((i == 0 && out != 0) || (i && out <= (uint64_t)index->list[i - 1].out)) { deflate_index_free(index); return NULL; }
    }
    return index;
}
static long source_size(FILE *in) { long here = ftell(in), end; if (fseek(in, 0, SEEK_END)) return -1; end = ftell(in); if (fseek(in, here, SEEK_SET)) return -1; return end; }
static int build(const char *source, const char *target, off_t span) {
    FILE *in = fopen(source, "rb"), *out; struct deflate_index *index = NULL; long bytes; int ret;
    if (in == NULL) return 2; bytes = source_size(in); if (bytes < 0 || fseek(in, 0, SEEK_SET)) { fclose(in); return 2; }
    ret = deflate_index_build(in, span, &index); fclose(in); if (ret < 0) { fprintf(stderr, "c97_zran: build %d\\n", ret); return 3; }
    out = fopen(target, "wb"); if (out == NULL) { deflate_index_free(index); return 2; }
    ret = write_index(out, index, (uint64_t)bytes, (uint64_t)span); fclose(out); fprintf(stderr, "c97_zran: built %d restart points\n", index->have); deflate_index_free(index); return ret ? 4 : 0;
}
static int extract(const char *source, const char *stored, off_t offset, size_t length) {
    FILE *in = fopen(source, "rb"), *idx = fopen(stored, "rb"); struct deflate_index *index; unsigned char *out; ptrdiff_t got; int lo = -1, hi;
    if (in == NULL || idx == NULL) return 2; index = read_index(idx); fclose(idx); if (index == NULL) { fclose(in); return 5; }
    hi = index->have; while (hi - lo > 1) { int mid = (lo + hi) >> 1; if (offset < index->list[mid].out) hi = mid; else lo = mid; }
    out = malloc(length ? length : 1); if (out == NULL) { fclose(in); deflate_index_free(index); return 6; }
    got = deflate_index_extract(in, index, offset, out, length); fclose(in);
    if (got < 0) { free(out); deflate_index_free(index); return 7; }
    if (fwrite(out, 1, (size_t)got, stdout) != (size_t)got) { free(out); deflate_index_free(index); return 8; }
    fprintf(stderr, "c97_zran: restart=%d compressed=%lld uncompressed=%lld bits=%d returned=%td\n", lo, (long long)index->list[lo].in, (long long)index->list[lo].out, index->list[lo].bits, got);
    free(out); deflate_index_free(index); return 0;
}
/* A bounded, reloadable worker.  It loads the persisted index once, then
 * accepts fixed-endian (u64 offset,u32 length) requests on stdin. */
static int serve(const char *source, const char *stored) {
    FILE *in = fopen(source, "rb"), *idx = fopen(stored, "rb"); struct deflate_index *index; uint64_t offset; uint32_t length; int lo, hi;
    if (in == NULL || idx == NULL) return 2; index = read_index(idx); fclose(idx); if (index == NULL) { fclose(in); return 5; }
    while (get_u64(stdin, &offset) == 0 && get_u32(stdin, &length) == 0) {
        unsigned char *out; ptrdiff_t got;
        lo = -1; hi = index->have; while (hi - lo > 1) { int mid = (lo + hi) >> 1; if ((off_t)offset < index->list[mid].out) hi = mid; else lo = mid; }
        out = malloc(length ? length : 1); if (out == NULL) { deflate_index_free(index); fclose(in); return 6; }
        got = deflate_index_extract(in, index, (off_t)offset, out, length);
        if (got < 0) fprintf(stderr, "c97_zran: serve extraction error %td at %llu\n", got, (unsigned long long)offset);
        if (got < 0) {
            if (put_u64(stdout, UINT64_MAX) || put_u32(stdout, (uint32_t)lo) || put_u64(stdout, (uint64_t)index->list[lo].in) || fflush(stdout)) { free(out); deflate_index_free(index); fclose(in); return 7; }
        }
        else if (put_u64(stdout, (uint64_t)got) || put_u32(stdout, (uint32_t)lo) || put_u64(stdout, (uint64_t)index->list[lo].in) ||
                 fwrite(out, 1, (size_t)got, stdout) != (size_t)got || fflush(stdout)) { free(out); deflate_index_free(index); fclose(in); return 7; }
        free(out);
    }
    deflate_index_free(index); fclose(in); return ferror(stdin) ? 8 : 0;
}
int main(int argc, char **argv) {
    if (argc >= 2 && !strcmp(argv[1], "build") && argc == 5) return build(argv[2], argv[3], (off_t)strtoll(argv[4], NULL, 10));
    if (argc >= 2 && !strcmp(argv[1], "extract") && argc == 6) return extract(argv[2], argv[3], (off_t)strtoll(argv[4], NULL, 10), (size_t)strtoull(argv[5], NULL, 10));
    if (argc == 4 && !strcmp(argv[1], "serve")) return serve(argv[2], argv[3]);
    if (argc == 2 && !strcmp(argv[1], "identity")) {
        uint16_t one = 1;
        printf("compile=%s\nruntime=%s\noff_t=%zu\nsize_t=%zu\nendianness=%s\n", ZLIB_VERSION, zlibVersion(), sizeof(off_t), sizeof(size_t), *(unsigned char *)&one ? "little" : "big");
        return 0;
    }
    fprintf(stderr, "usage: c97_zran build GZIP INDEX SPAN | extract GZIP INDEX OFFSET LENGTH\n"); return 64;
}
