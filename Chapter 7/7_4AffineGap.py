import sys
import numpy as np
from Bio.SubsMat import MatrixInfo as matlist 
similarityMatrixMap = matlist.blosum62
sys.setrecursionlimit(2000)
with open ('7_4.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
g = -11
e = -1
#print v, w
"""
TAGGCTTA
TAGA--TA
"""
v = 'PRTEINS'
w = 'PRTWPSEIN'
#print matrix

#v =  'TCTAGATGAGGGTGCCTTTCGTGTAGCTGATTTCCATGTGGATCACTTATACAGTCCCGGGGGATCGTGTGGGACTTAAAACGAGAATTGGCAGGCCTCAATAGACCCTATGATGAAATGTCACGGGCCGACTGGGATAGGAGGCGACCGACTACTCTAGCGCACACGAACCTGGTTGATTTGATTGGCACACATTCATATCCATGATGTCAGAACGAGACTTGCACAGGTAACGACCACTTAAATAGGTAGATCCAGATCGATCAGCTAATCTGTAACAGCGCAAGTGGCTTCTTGCAGATGGCTCCTGTGTGAAACACAGCGATGATCTCGCATTGACCGCCTTGCAGTGGTGTCCTCTTAACTGAAGCTCGATATCACATCACAGTGTGAGAAAATCCGGGGGCATTGCCTACGTCGCTGATTGTCATTCTTGCAGTGTGATGCAGTCGTGTTGAAGTACGGGGAATATTTGAGTCAAAGTTGGAGGATTCTCAAGAGGTCTGTTCTACGGGCTAGAGCTATCTCATTTCGCTGCCCAGTGGTCAAAGGCGAATCGACTCACTGAAGTAGTTAGGGGAACAGTCCTTCATTTGACATTATGAGGAACCTTAATCTTTGTGCTCTGTATTTCTTCTTCCCAAGGGTATTTCTCATTAGGACATTACGCTAGTACTGTAAACTCCATATAGTGGCGGAATAATCCTGGGCCAGTTATGTGATGCCCTGTCTTGAGATTTGGAAGCGCCTCTTTGCCTCTATTACATATGGCACAGGATACAGCCAAACTGCACGTCGGTTGGTACCCTCCCAACTCCGAGATGTGTTATTGCTAGTTCGGCACGCAGAGATAGAACCTAATATCGCCACATGTGACGAAGCAC'
     
    #seq2 = 'PENALTY'
#w = 'CTACGTAGCCCGTTCGTCATGCCGGGTGAGTTAAGGCGTCCGTAATGGTAGTCTGTTTTTTTGCAAAGTATGGTAACCTAG'
def AffineGap(v, w):
    n = len(v); m = len(w)
    backtrack = np.zeros((n + 1,m + 1),int)
    V = np.zeros((n + 1,m + 1),int)
    F = np.zeros((n + 1,m + 1),int)
    E = np.zeros((n + 1,m + 1),int)
    M = np.zeros((n + 1,m + 1),int)
    V[0][0] = 0;F[0][0] = 0;E[0][0] = 0;M[0][0] = 0;
    for i in range(1, n + 1):
        V[i][0] = M[i][0] = E[i][0] = g + (i-1)*e
    for j in range(1, m + 1):
        V[0][j] = M[0][j] = F[0][j] = g + (j-1)*e
    
    for i in range(1, n + 1):
        for j in range(1, m + 1): 
            if (v[i-1], w[j-1]) in similarityMatrixMap:
                M[i][j] = V[i-1][j-1] + similarityMatrixMap[(v[i-1], w[j-1])]
            elif (w[j-1], v[i-1]) in similarityMatrixMap:
                M[i][j] = V[i-1][j-1] + similarityMatrixMap[(w[j-1], v[i-1])]
            F[i][j] = max(M[i-1][j] + g, F[i-1][j] + e)
            E[i][j] = max(M[i][j-1] + g, E[i][j-1] + e)
            V[i][j] = max(E[i][j], F[i][j], M[i][j])
            #print down[i-1][j], right[i][j-1]
            if V[i][j] == E[i][j]:
                  backtrack[i][j] = 3
            elif V[i][j] == F[i][j]:
                  backtrack[i][j] = 2
            elif V[i][j] == M[i][j]:
                  backtrack[i][j] = 1
    print V[-1][-1]#, V
    return backtrack
"""            
    Best = max([V[n][i] for i in range(0, m + 1)])
    for i in range(0, m + 1):
        if Best == V[n][i]:
            Endi = n
            Endj = i
            break
"""
   # Endi = 9
   # Endj = 6
   # print Best#, Endi, Endj#, backtrack
    
seq1 = []
seq2 = []
def OUTPUTGap(backtrack, v, w, i, j): 
        #print seq1, seq2, i, j, backtrack[i][j]
    if i == 0 and j ==0:
            return
    else:    
        if backtrack[i][j] == 1:
            OUTPUTGap(backtrack, v, w, i-1, j-1)
            print i, j
            seq1.append(v[i-1])
            seq2.append(w[j-1])    
        elif backtrack[i][j] == 2:
            OUTPUTGap(backtrack, v, w, i-1, j)
            print i, j
            #print i-1, v[i-1]
            seq1.append(v[i-1])
            seq2.append('-')
        elif backtrack[i][j] == 3:
            OUTPUTGap(backtrack, v, w, i, j - 1)  
            print i, j
            seq1.append('-')
            seq2.append(w[j-1])
        return ''.join(seq1), ''.join(seq2)
backtrack = AffineGap(v,w)
align1, align2 = OUTPUTGap(backtrack, v, w, len(v), len(w))
print align1
print align2

"""
Define the matrices V, E, F, and M as follows:

M(i,j) = Optimal sequence alignment of X1X2...Xi and Y1Y2...Yj such
	 that Xi is aligned to Yj
E(i,j) = Optimal sequence alignment of X1X2...Xi and Y1Y2...Yj such
	 that Yj is aligned to a gap
F(i,j) = Optimal sequence alignment of X1X2...Xi and Y1Y2...Yj such
	 that Xi is aligned to a gap
V(i,j) = Optimal sequence alignment of X1X2...Xi and Y1Y2...Yj 

Initialization:

V(0,0) = 0
V(i,0) = M(i,0) = E(i,0) = g+(i-1)e
V(0,j) = M(0,j) = F(0,j) = g+(j-1)e

Recurrence:

V(i,j) = max{ E(i,j), F(i,j), M(i,j) )
M(i,j) = V(i-1,j-1) + m/mm
F(i,j) = max{ M(i-1,j) + g, F(i-1,j) + e }
E(i,j) = max{ M(i,j-1) + g, E(i,j-1) + e }
"""