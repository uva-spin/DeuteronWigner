! Compile against vendored arTeMiDe v2.05 to validate BPV20 evolution.
program bpv20_artemide_probe
  use aTMDe_control
  use TMDs
  use TMDs_inKT
  implicit none
  real*8 :: p(14), opt(-5:5), evolved(-5:5), kt(-5:5)
  real*8 :: x, b, q, transverse_momentum

  p = (/ 0.5362d0, 5.21724d0, 202.749d0, 0.d0, 0.d0, &
       -0.01661d0, -0.35169d0, -3.90804d0, 0.37263d0, &
       -0.70153d0, 8.97236d0, 0.75803d0, 2.46253d0, -0.47481d0 /)
  x = 0.1d0
  b = 1.d0
  q = 5.d0
  transverse_momentum = 0.5d0

  call artemide_Initialize('const-BPV20_n3lo-proton-sivers', &
       prefix='build/artemide/')
  call artemide_SetNPparameters_SiversTMDPDF(p)
  opt = SiversTMDPDF_5(x, b, 1)
  evolved = SiversTMDPDF_5(x, b, q, q*q, 1)
  kt = SiversTMDPDF_kT_5(x, transverse_momentum, q, q*q, 1)
  write(*,'(A,5(ES24.16,1X))') 'OPT ', opt(2), opt(1), opt(-2), opt(-1), opt(3)
  write(*,'(A,5(ES24.16,1X))') 'EVOLVED ', evolved(2), evolved(1), &
       evolved(-2), evolved(-1), evolved(3)
  write(*,'(A,5(ES24.16,1X))') 'KT ', kt(2), kt(1), kt(-2), kt(-1), kt(3)
end program bpv20_artemide_probe
