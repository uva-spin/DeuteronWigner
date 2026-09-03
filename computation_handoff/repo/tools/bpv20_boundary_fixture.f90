! Independent numerical fixture for the public BPV20 FNP formula.
program bpv20_boundary_fixture
  implicit none
  integer, parameter :: dp = selected_real_kind(15, 307)
  real(dp) :: l(14), x, b, yy, profile
  real(dp) :: normu, normd, norms, fu, fd, fsea, fs
  l = (/ 0.5362_dp, 5.21724_dp, 202.749_dp, 0._dp, 0._dp, &
       -0.01661_dp, -0.35169_dp, -3.90804_dp, 0.37263_dp, &
       -0.70153_dp, 8.97236_dp, 0.75803_dp, 2.46253_dp, -0.47481_dp /)
  x = 0.1_dp
  b = 1._dp
  yy = (l(1) + x*l(2))*b**2/sqrt(1._dp + abs(l(3))*x**2*b**2)
  profile = exp(-yy)
  normu = (3._dp+l(7)+l(8)*(1._dp+l(7))) / &
          ((l(7)+1._dp)*(l(7)+2._dp)*(l(7)+3._dp))
  normd = (3._dp+l(10)+l(11)*(1._dp+l(10))) / &
          ((l(10)+1._dp)*(l(10)+2._dp)*(l(10)+3._dp))
  norms = 1._dp/((l(13)+1._dp)*(l(13)+2._dp))
  fu = l(6)*(1._dp-x)*x**l(7)*(1._dp+l(8)*x)/normu
  fd = l(9)*(1._dp-x)*x**l(10)*(1._dp+l(11)*x)/normd
  fs = l(12)*(1._dp-x)*x**l(13)/norms
  fsea = l(14)*(1._dp-x)*x**l(13)/norms
  write(*,'(5(ES24.16,1X))') profile*fu, profile*fd, &
       profile*fsea, profile*fsea, profile*fs
end program bpv20_boundary_fixture
