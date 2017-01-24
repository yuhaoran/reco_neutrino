implicit none
include 'mpif.h'
integer(4) :: i,j,k,l,m,n,ierr,fstat,rank
real(4) :: a,b,c,d,e,f,g
character (len=6) :: rank_s
character (len=100) :: fn
call mpi_init(ierr)
call mpi_comm_size(mpi_comm_world,n,ierr)
call mpi_comm_rank(mpi_comm_world,rank,ierr)
write(rank_s,'(i6)') rank; rank_s=adjustl(rank_s)
fn='./test/file_'//trim(rank_s)//'.dat'
do i=1,10000
  open(11,file=fn,iostat=fstat,access='stream')
  if (fstat /= 0) then
    call system('hostname')
  endif
  close(11)
enddo
if (rank==0) print*,'done'
call mpi_finalize(ierr)
end
