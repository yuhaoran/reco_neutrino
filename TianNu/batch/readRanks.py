import numpy

x1 = numpy.array([ ], dtype="int32")
x2 = numpy.array([ ], dtype="int32")

fr1 = open("rankStartLog_28_3", "r")
fr2 = open("rankStopLog_28_3", "r")
l1 = fr1.readlines()
l2 = fr2.readlines()
fr1.close()
fr2.close()

for i in xrange(len(l1)):

    cline = str.split(l1[i])
    x1 = numpy.append(x1, int(cline[-1]))

for i in xrange(len(l2)):

    cline = str.split(l2[i])
    x2 = numpy.append(x2, int(cline[-1]))


N = 13824

print "NOT IN X1:"
for i in xrange(N):
    if i not in x1: print i

c = 0
print "NOT IN X2:"
bad = numpy.array([ ], dtype="int32")
for i in xrange(N):
    if i not in x2: 
        bad = numpy.append(bad, i)
        print i
        c += 1

print "c = ", c
print bad - numpy.roll(bad,1)

