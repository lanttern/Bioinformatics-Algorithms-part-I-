import sys
from Bio.SubsMat import MatrixInfo as matlist 
sys.setrecursionlimit(2000)
with open ('6_6.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
#print v, w
matrix = matlist.pam250
#print matrix
gap = -5
#v =  'AAAAAASSSSSSSVVVVVVVVTTTTTTTLLLLLL'
     
    #seq2 = 'PENALTY'
#w = 'SSSSLLLLLTTTTTTTWWWWWWWWWWWPPPPPPPPPP'
def LCS(v, w):
    n = len(v); m = len(w)
    s = [[0]*(m + 1) for i in range(n + 1)]
    backtrack = [[0]*(m + 1) for i in range(n + 1)]
    Best = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #print down[i-1][j], right[i][j-1]
            if (v[i-1], w[j-1]) in matrix:
               s[i][j] =max(s[i-1][j] + gap, s[i][j-1] + gap, s[i-1][j-1] + matrix[(v[i-1], w[j-1])], 0)
            if (w[j-1], v[i-1]) in matrix:
               s[i][j] =max(s[i-1][j] + gap, s[i][j-1] + gap, s[i-1][j-1] + matrix[(w[j-1], v[i-1])], 0)            
            if s[i][j] == 0:
                backtrack[i][j] = 0
            if (v[i-1], w[j-1]) in matrix:
                if s[i][j] == s[i-1][j-1] + matrix[(v[i-1], w[j-1])]:
                    backtrack[i][j] = 1
            if (w[j-1], v[i-1]) in matrix:
                if s[i][j] == s[i-1][j-1] + matrix[(w[j-1], v[i-1])]:
                    backtrack[i][j] = 1
            if s[i][j] == s[i-1][j] + gap:
               backtrack[i][j] = 2
            if s[i][j] == s[i][j-1] + gap:
               backtrack[i][j] = 3 
            if s[i][j] > Best:
                 Best = s[i][j]
                 Endi = i
                 Endj = j
            
    print Best
    return backtrack, Endi, Endj
seq1 = []
seq2 = []
def OUTPUTLCS(backtrack, v, w, i, j): 
        #print seq1, seq2, i, j, backtrack[i][j]
        if backtrack[i][j] == 0:
            return
        if backtrack[i][j] == 1:
            OUTPUTLCS(backtrack, v, w, i-1, j-1)
            seq1.append(v[i-1])
            seq2.append(w[j-1])
        elif backtrack[i][j] == 2:
            OUTPUTLCS(backtrack, v, w, i-1, j)
            seq1.append(v[i-1])
            seq2.append('-')
        elif backtrack[i][j] == 3:
            OUTPUTLCS(backtrack, v, w, i, j - 1)  
            seq1.append('-')
            seq2.append(w[j-1])
        return ''.join(seq1), ''.join(seq2)
backtrack, i, j = LCS(v,w)
align1, align2 = OUTPUTLCS(backtrack, v, w, i, j)
print align1
print align2
   
