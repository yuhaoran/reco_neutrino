import numpy

# ----------------------- parameters -----------------------

# Parameters that we need
nodes_dim      = 2
tiles_node_dim = 4
nf_tile        = 176 
density_buffer = 1.5
ratio_nudm_dim = 2

# Set this true if using P3DFFT for pencil decomposition
pencil = True

# Usually won't need to change these
nf_cutoff   = 16
nf_buf      = nf_cutoff + 8

# ----------------------------------------------------------

#
# Compute values that we need
#

nc = (nf_tile - 2 * nf_buf) * tiles_node_dim * nodes_dim
nodes = nodes_dim**3
nc_node_dim = nc / nodes_dim
nc_pen = nc_node_dim / nodes_dim
nc_slab = nc / nodes
nodes_pen = nodes_dim
nodes_slab = nodes_dim**2

max_np  = int(density_buffer * (((nf_tile - 2 * nf_buf) * tiles_node_dim / 2)**3 + \
    (8 * nf_buf**3 + 6 * nf_buf * (((nf_tile - 2 * nf_buf) * tiles_node_dim)**2) + \
    12 * (nf_buf**2) * ((nf_tile - 2 * nf_buf) * tiles_node_dim)) / 8.))
np_buffer = int(2.*max_np/3.)

print
print "Sizes of various variables:"
print "nc          = ", nc
print "nc_node_dim = ", nc_node_dim
print "nc_slab     = ", nc_slab
print "nc_pen      = ", nc_pen
print "max_np      = ", max_np
print "np_buffer   = ", np_buffer

#
# Size of equivalence arrays declared in cic_mompower_p3dfft.f90 
#

print
print "Checking equivalence statements in cic_mompower_p3dfft.f90 ... "
print

# First statement (recv_cube, xp_buf) 

if pencil:
    recv_cube = 4 * (nc_node_dim**2 * nc_pen * nodes_pen) 
else:
    recv_cube = 4 * (nc_node_dim**2 * nc_slab * nodes_slab)
xp_buf = 6 * np_buffer

maxeq1 = max(recv_cube, xp_buf)

if maxeq1 != recv_cube:

    print "Change equivalence and common block accordingly:"
    print "recv_cube = ", recv_cube
    print "xp_buf    = ", xp_buf
    print

# Second statement (momden, send_buf)

momden = 4 * (1 * (nc_node_dim+2)**3)
send_buf = 4 * (6*np_buffer)

maxeq2 = max(momden, send_buf)

if maxeq2 != momden:

    print "Change equivalence and common block accordingly:"
    print "momden   = ", momden
    print "send_buf = ", send_buf
    print

# Third statement (only used if SLAB is true)

if pencil:
    slab_work = 0
else:
    slab_work = 4 * ((nc + 2) * nc * nc_slab)
recv_buf = 6*np_buffer

maxeq3 = max(slab_work, recv_buf)

if not pencil and maxeq3 != slab_work:

    print "Change equivalence and common block accordingly:"
    print "slab_work = ", slab_work
    print "recv_buf  = ", recv_buf
    print

#
# Compute size of the other equivalence statements that won't change 
#

if pencil:
    slab = 4 * (nc * nc_node_dim * (nc_pen + 2))
else:
    slab = 4 * ((nc + 2) * nc * nc_slab)
massden_send_buff = 4 *(nc_node_dim+2)**2
massden_recv_buff = 4 *(nc_node_dim+2)**2

maxeq4 = slab 
maxeq5 = massden_send_buff
maxeq6 = massden_recv_buff

#
# Compute the sizes of other big arrays
#

xvp = 4 * (6 * max_np)
xvp_dm = xvp / ratio_nudm_dim**3
massden = 4 * (nc_node_dim+2)**3

print "Total memory used by large arrays [GB]: ", (maxeq1 + maxeq2 + maxeq3 + maxeq4 + maxeq5 + maxeq6 + xvp + xvp_dm + massden) / 1024.**3
print

