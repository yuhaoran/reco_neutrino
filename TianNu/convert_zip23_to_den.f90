implicit none
include 'mpif.h'

integer, parameter :: nc3=288**3
integer :: rank, nrank, ierr
integer(1) :: iden1(4,nc3)
integer(4) :: iden4(nc3), i4(nc3/8), i,j,k,l,m,n
real(4) :: rden(nc3)
character(8) :: rank_s
character(300) :: fn2,fn3,fnden, fn2nu, fn3nu,fndennu

equivalence(iden1,iden4)

call mpi_init(ierr)
call mpi_comm_size(mpi_comm_world,nrank,ierr)
call mpi_comm_rank(mpi_comm_world,rank,ierr)
write(rank_s,'(i8)') rank
rank_s=adjustl(rank_s)
fn2='/WORK/bnu_ztj_1/yuanshuo/tildes/LOS29-3/node'//trim(rank_s)//'/0.010zip2_'//trim(rank_s)//'.dat'
fn3='/WORK/bnu_ztj_1/yuanshuo/tildes/LOS29-3/node'//trim(rank_s)//'/0.010zip3_'//trim(rank_s)//'.dat'
fnden='/WORK/bnu_ztj_1/yuanshuo/tildes/coarse_den_real/0.010den_'//trim(rank_s)//'.dat'
fn2nu='/WORK/bnu_ztj_1/yuanshuo/tildes/LOS29-3/node'//trim(rank_s)//'/0.010zip2_'//trim(rank_s)//'_nu.dat'
fn3nu='/WORK/bnu_ztj_1/yuanshuo/tildes/LOS29-3/node'//trim(rank_s)//'/0.010zip3_'//trim(rank_s)//'_nu.dat'
fndennu='/WORK/bnu_ztj_1/yuanshuo/tildes/coarse_den_real/0.010den_'//trim(rank_s)//'_nu.dat'


!! DM
iden1=0; i4=0
open(12,file=fn2,status='old',access='stream',buffered='yes')
open(13,file=fn3,status='old',access='stream',buffered='yes')
read(12) iden1(1,:) ! for big endian, iden(4,:)
read(13,end=701) i4(count(iden4==255))
701 close(12); close(13)

j=0
do i=1,nc3
  if (iden4(i)==255) then
    j=j+1
    iden4(i)=i4(j)
  endif
enddo
rden=iden4
!print*,trim(adjustl(fnden)),': min, max ='
!print*,minval(rden),maxval(rden)

open(15,file=fnden,status='replace',access='stream',buffered='yes')
write(15) rden
close(15)

!!NU
iden1=0; i4=0
open(12,file=fn2nu,status='old',access='stream',buffered='yes')
open(13,file=fn3nu,status='old',access='stream',buffered='yes')
read(12) iden1(1,:) ! for big endian, iden(4,:)
read(13,end=702) i4(count(iden4==255))
702 close(12); close(13)

j=0
do i=1,nc3
  if (iden4(i)==255) then
    j=j+1
    iden4(i)=i4(j)
  endif
enddo
rden=iden4

!print*,trim(adjustl(fnden)),': min, max ='
!print*,minval(rden),maxval(rden)
open(15,file=fndennu,status='replace',access='stream',buffered='yes')
write(15) rden/8
close(15)

call mpi_finalize(ierr)

end
