import numpy

numfiles = 576

fr = open("yhqlist.dat", "r")
lines = fr.readlines()
fr.close()

cline = str.split(lines[1])[-1]
gline = cline.replace("cn[", "")
gline = gline.replace("]", "")
gline = gline.split(",")

nodes = numpy.array([ ], dtype="int32")

for i in xrange(len(gline)):

    xx = gline[i] 

    if "-" in xx:
        yy = xx.split("-")
	zz = numpy.array(range(int(yy[0]), int(yy[1])+1),dtype=nodes.dtype)
	nodes = numpy.append(nodes, zz)
    else:
        nodes = numpy.append(nodes, int(xx))

if nodes.shape[0]%numfiles != 0: print "Cannot decompose into ", numfiles

nn = nodes.shape[0]/numfiles

print nodes.shape
print numfiles

nodes = nodes.reshape(numfiles, nn)

for i in xrange(nodes.shape[0]):

    if i%24 == 0: print "writing for i = ", i
    ofile = "./nodelist/list" + str(i).zfill(3) + ".dat"
    fw = open(ofile, "w")
    for j in xrange(nn):
        s = "cn" + str(nodes[i][j]) + "\n"
        fw.write(s)
    fw.close()

