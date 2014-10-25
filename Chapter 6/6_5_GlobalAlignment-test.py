from Bio.SubsMat import MatrixInfo as matlist
matrix = matlist.blosum62

with open ('6_5.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
#print v, w
delta = 5
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
matrix = matlist.blosum62
d = pairwise2.align.globaldx(v, w, matrix)
gap = d[0][0].count('-') + d[0][1].count('-')
score = d[0][2] - delta*gap
print int(score)
print d
#print d[0][0]
#print d[0][1]