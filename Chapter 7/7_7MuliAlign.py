import sys
import numpy as np
#from Bio.SubsMat import MatrixInfo as matlist 
sys.setrecursionlimit(2000)
with open ('7_7.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
    z = (r.readline()).translate(None, '\n')
#print v, w
#v = "ATATCCG"
#w = "TCCGA"
#z = "ATGTACTG"
#similarityMatrixMap = matlist.blosum62
#g1, g2, g3, g4, g5, g6, g7 = -1, -2, -3, -4, -5, -6, -7
def MidEdge(seq1, seq2, seq3, gap):
    '''This function creates alignment score matrix
    seq1 : reference sequence
    seq2 : other sequence
    gap : gap penalty '''
 
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    n = len(seq3) + 1
    s = np.zeros((rows,cols, n),int)
    backtrack = np.zeros((rows, cols, n),int)
    for i in range(0, rows):
        s[i][0][0] = -i
    for j in range(0, cols):
        s[0][j][0] = -j
    for k in range(0, n):
        s[0][0][k] = -k  
    #print s
    for i in range(1, rows):
        for j in range(1, cols):
            for k in range(1, n):
               if v[i-1] == w[j-1] == z[k-1]: 
                  s[i][j][k] = max(s[i-1][j][k], s[i][j-1][k], s[i][j][k-1], s[i-1][j-1][k], s[i][j-1][k-1],s[i-1][j][k-1], s[i-1][j-1][k-1] + 1)
               else: 
                  s[i][j][k] = max(s[i-1][j][k], s[i][j-1][k], s[i][j][k-1], s[i-1][j-1][k], s[i][j-1][k-1],s[i-1][j][k-1], s[i-1][j-1][k-1])               
               if s[i][j][k] == (s[i-1][j-1][k-1] + 1 and v[i-1] == w[j-1] == z[k-1]) or s[i][j][k] == s[i-1][j-1][k-1]:
                   backtrack[i][j][k] = 1
               elif s[i][j][k] == s[i-1][j][k-1]:
                   backtrack[i][j][k] = 2
               elif s[i][j][k] == s[i][j-1][k-1]:
                   backtrack[i][j][k] = 3
               elif s[i][j][k] == s[i-1][j-1][k]:
                   backtrack[i][j][k] = 4
               elif s[i][j][k] == s[i][j][k-1]:
                   backtrack[i][j][k] = 5
               elif s[i][j][k] == s[i][j-1][k]:
                   backtrack[i][j][k] = 6
               elif s[i][j][k] == s[i-1][j][k]:
                   backtrack[i][j][k] = 7
               elif s[i][j][k] == s[i-1][j-1][k-1] + 1 or s[i][j][k] == s[i-1][j-1][k-1]:
                   backtrack[i][j][k] = 1
               
              
               
               
               
               
               
               
               
               
    print  s[-1][-1][-1]
    return backtrack
seqA = []
seqB = []  
seqC = []  
def OUTPUTMidEdge(backtrack, i, j, k, v, w, z): 
    #print seqA, seqB, i, j, backtrack[i][j]
    if i == 0 and j ==0 and k == 0:
        return  
    else:
      if backtrack[i][j][k] == 1:
            #print v[i-1], w[j-1], z[k-1]
            OUTPUTMidEdge(backtrack, i-1, j-1, k-1, v, w, z)
            seqA.append(v[i-1])
            seqB.append(w[j-1])
            seqC.append(z[k-1])
               
      elif backtrack[i][j][k] == 2:
            OUTPUTMidEdge(backtrack, i-1, j, k-1, v, w, z)
            seqA.append(v[i-1])
            seqB.append('-')
            seqC.append(z[k-1])
      elif backtrack[i][j][k] == 3:
            OUTPUTMidEdge(backtrack, i, j - 1, k-1, v, w, z)  
            seqA.append('-')
            seqB.append(w[j-1])
            seqC.append(z[k-1])
      elif backtrack[i][j][k] == 4:
            OUTPUTMidEdge(backtrack, i-1, j - 1, k, v, w, z)  
            seqA.append(v[i-1])
            seqB.append(w[j-1])
            seqC.append('-')
      elif backtrack[i][j][k] == 5:
            OUTPUTMidEdge(backtrack, i, j, k-1, v, w, z)
            seqA.append('-')
            seqB.append('-')
            seqC.append(z[k-1])
      elif backtrack[i][j][k] == 6:   
            OUTPUTMidEdge(backtrack, i, j - 1, k, v, w, z)  
            seqA.append('-')
            seqB.append(w[j-1])
            seqC.append('-')
      elif backtrack[i][j][k] == 7:   
            OUTPUTMidEdge(backtrack, i-1, j, k, v, w, z)  
            seqA.append(v[i-1])
            seqB.append('-')
            seqC.append('-')
      else:
          if i > 0 and j > 0 and k==0:
            backtrack[i][j][k] = 4
            OUTPUTMidEdge(backtrack, i-1, j - 1, k, v, w, z)  
            seqA.append(v[i-1])
            seqB.append(w[j-1])
            seqC.append('-')
          if i > 0 and j == 0 and k > 0:
            backtrack[i][j][k] = 2
            OUTPUTMidEdge(backtrack, i-1, j, k-1, v, w, z)
            seqA.append(v[i-1])
            seqB.append('-')
            seqC.append(z[k-1]) 
          if i == 0 and j > 0 and k > 0:
            backtrack[i][j][k] = 3
            OUTPUTMidEdge(backtrack, i, j - 1, k-1, v, w, z)  
            seqA.append('-')
            seqB.append(w[j-1])
            seqC.append(z[k-1]) 
          if i == 0 and j == 0 and k > 0:
            backtrack[i][j][k] = 5
            OUTPUTMidEdge(backtrack, i, j, k-1, v, w, z)
            seqA.append('-')
            seqB.append('-')
            seqC.append(z[k-1])
          if i == 0 and j > 0 and k == 0:
            backtrack[i][j][k] = 6
            OUTPUTMidEdge(backtrack, i, j - 1, k, v, w, z)  
            seqA.append('-')
            seqB.append(w[j-1])
            seqC.append('-')
          if i > 0 and j == 0 and k == 0:
            backtrack[i][j][k] = 7
            OUTPUTMidEdge(backtrack, i-1, j, k, v, w, z)  
            seqA.append(v[i-1])
            seqB.append('-')
            seqC.append('-')
            #print backtrack[i][j][k], i, j, k
      return ''.join(seqA), ''.join(seqB), ''.join(seqC)
            
A, B, C = OUTPUTMidEdge(MidEdge(v, w, z, 0), len(v), len(w), len(z), v, w, z)
print A
print B
print C
