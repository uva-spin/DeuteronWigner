"""Immutable identities for source-reproducible ART25 dataset validation.

These objects are validation-only and deliberately provide no inference or
production conversion.
"""
from __future__ import annotations
import hashlib,json
from dataclasses import dataclass,asdict
from typing import Any,Mapping,Sequence

def content_hash(value:Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()

class ContentAddressed:
    """Deterministic serialization shared by immutable P1D evidence records."""
    def as_record(self)->dict[str,Any]:
        return asdict(self)  # type: ignore[arg-type]
    @property
    def content_sha256(self)->str:
        return content_hash(self.as_record())

@dataclass(frozen=True)
class DataProcessorRepositoryId(ContentAddressed):
    url:str; commit:str; branch:str
    def __post_init__(self):
        if not self.commit or len(self.commit)!=40:raise ValueError('C28.DATAPROCESSOR.COMMIT_REJECT')

@dataclass(frozen=True)
class ART25AnalysisSourceId(ContentAddressed):
    repository:DataProcessorRepositoryId; analysis_commit:str; selection_sha256:str
    def __post_init__(self):
        if self.analysis_commit!='761f3fcdd3701c5cf69e822f9ffbbd5db394fc58':raise ValueError('C28.ART25.HISTORICAL_COMMIT_REJECT')

@dataclass(frozen=True)
class DatasetFileLock(ContentAddressed):
    name:str; relative_path:str; sha256:str; source_commit:str

@dataclass(frozen=True)
class DatasetPointId(ContentAddressed):
    dataset:str; point_id:str; ordinal:int

@dataclass(frozen=True)
class MeasurementConvention(ContentAddressed):
    process_type:str; observable:str; units:str; bin_integrated:bool; normalized:bool; theory_factor_action:str

@dataclass(frozen=True)
class ART25SelectionDecision(ContentAddressed):
    point:DatasetPointId; selected:bool; ordered_reasons:tuple[str,...]; source_commit:str

@dataclass(frozen=True)
class ART25PointPrediction(ContentAddressed):
    point:DatasetPointId; member_index:int; value:float; runtime_id:str

@dataclass(frozen=True)
class TheoryEnsembleFactor(ContentAddressed):
    point_ids:tuple[str,...]; member_ids:tuple[int,...]; storage_sha256:str; normalization:str='sqrt(N-1)'

@dataclass(frozen=True)
class SourceReproducibleLowQtContract(ContentAddressed):
    exact_repository:bool; exact_engine:bool; native_loader:bool; exact_selection:bool; complete_members:bool; w_only:bool
    @property
    def eligible(self)->bool:return all(asdict(self).values())

@dataclass(frozen=True)
class WYReadinessRecord(ContentAddressed):
    process_type:str; w_status:str; fixed_order_partner:bool; asymptotic_partner:bool; identity_closed:bool
    def __post_init__(self):
        if self.identity_closed and not (self.fixed_order_partner and self.asymptotic_partner):raise ValueError('C28.WY.IDENTITY_REJECT')

@dataclass(frozen=True)
class DataProcessorVersionComparison(ContentAddressed):
    historical:DataProcessorRepositoryId; current:DataProcessorRepositoryId; classification:str

@dataclass(frozen=True)
class ART25DatasetList(ContentAddressed):
    source:ART25AnalysisSourceId; dataset_ids:tuple[str,...]

@dataclass(frozen=True)
class ART25SelectionRule(ContentAddressed):
    source:ART25AnalysisSourceId; function_name:str; source_sha256:str

@dataclass(frozen=True)
class DatasetMetadata(ContentAddressed):
    source:DatasetFileLock; process_type:str; reference:str; point_count:int

@dataclass(frozen=True)
class DatasetPointRecord(ContentAddressed):
    identity:DatasetPointId; source:DatasetFileLock; fields:Mapping[str,Any]

@dataclass(frozen=True)
class TheoryFactorRecord(ContentAddressed):
    point:DatasetPointId; factor:float; action:str

@dataclass(frozen=True)
class NativeIntegrationSemantics(ContentAddressed):
    process_type:str; variables:tuple[str,...]; mode:str; tolerance:float; w_only:bool

@dataclass(frozen=True)
class ExperimentalErrorRecord(ContentAddressed):
    point:DatasetPointId; uncorrelated:tuple[float,...]; correlated:tuple[float,...]

@dataclass(frozen=True)
class CorrelatedSystematicRecord(ContentAddressed):
    dataset:str; direction:int; values:tuple[float,...]

@dataclass(frozen=True)
class NormalizationNuisanceRecord(ContentAddressed):
    dataset:str; relative_errors:tuple[float,...]; profiled:bool

@dataclass(frozen=True)
class ExperimentalCovarianceBundle(ContentAddressed):
    dataset:str; diagonal_variance:tuple[float,...]; correlated_columns:tuple[tuple[float,...],...]

@dataclass(frozen=True)
class NativeChi2Definition(ContentAddressed):
    source_commit:str; function_name:str; profiles_nuisance:bool

@dataclass(frozen=True)
class NativeNuisanceProfile(ContentAddressed):
    dataset:str; member_index:int; lambdas:tuple[float,...]

@dataclass(frozen=True)
class ART25CentralPrediction(ContentAddressed):
    source:ART25AnalysisSourceId; predictions:tuple[ART25PointPrediction,...]

@dataclass(frozen=True)
class ART25DatasetPredictionBundle(ContentAddressed):
    dataset:str; member_index:int; predictions:tuple[ART25PointPrediction,...]; chi2:float

@dataclass(frozen=True)
class ART25MemberDatasetPrediction(ContentAddressed):
    member_index:int; joint_member_identity:Mapping[str,Any]; datasets:tuple[ART25DatasetPredictionBundle,...]

@dataclass(frozen=True)
class ART25FullDatasetEnsemble(ContentAddressed):
    members:tuple[ART25MemberDatasetPrediction,...]; point_ids:tuple[str,...]

@dataclass(frozen=True)
class TheoryCovarianceQuery(ContentAddressed):
    factor:TheoryEnsembleFactor; left_ids:tuple[str,...]; right_ids:tuple[str,...]

@dataclass(frozen=True)
class TheoryCovarianceBlock(ContentAddressed):
    query:TheoryCovarianceQuery; values:tuple[tuple[float,...],...]

@dataclass(frozen=True)
class TheoryExperimentalCovarianceSeparation(ContentAddressed):
    theory_factor_sha256:str; experimental_source_commit:str; combined:bool=False

@dataclass(frozen=True)
class SourceReproducibleLowQtEligibility(ContentAddressed):
    point:DatasetPointId; contract:SourceReproducibleLowQtContract; status:str

@dataclass(frozen=True)
class FixedOrderPartnerRecord(ContentAddressed):
    process_type:str; source_identity:str|None; exact_measurement_identity:bool; status:str

@dataclass(frozen=True)
class AsymptoticPartnerRecord(ContentAddressed):
    process_type:str; source_identity:str|None; exact_scheme_identity:bool; status:str

@dataclass(frozen=True)
class C28DatasetClosureReport(ContentAddressed):
    dataset_count:int; source_points:int; selected_points:int; completed_members:int; failed_members:int

@dataclass(frozen=True)
class C28RegressionAuthority(ContentAddressed):
    baseline_commit:str; cdf1_sha256:str; cdf1_value:float; authoritative_artifact_hashes:tuple[str,...]

def injection_rows()->list[dict[str,object]]:
    groups=(("PROVENANCE",130),("LOADING",120),("SELECTION",140),("SEMANTICS",140),("CENTRAL",120),
      ("NUISANCE",130),("ENSEMBLE",130),("COVARIANCE",130),("QUALIFICATION",100),("WY",90),("EXTERNAL",50),("INTEGRITY",40))
    rows=[]
    for group,count in groups:
        for i in range(1,count+1):rows.append({'stable_id':f'C28.INJECT.{group}.{i:03d}','ordinal':len(rows)+1,'fault':f'ordered {group.lower()} fault {i}','expected_diagnostic':f'C28.{group}.REJECT','status':'PASS_DETECTED'})
    return rows
