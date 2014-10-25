import sys
sys.setrecursionlimit(2000)

with open ('6_3.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
#print v, w

def LCS(v, w):
    n = len(v); m = len(w)
    s = [[0]*(m + 1) for i in range(n + 1)]
    backtrack = [[0]*(m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #print down[i-1][j], right[i][j-1]
            if v[i-1] == w[j-1]:
                s[i][j] =max(s[i-1][j], s[i][j-1], s[i-1][j-1] + 1)
            else:
                s[i][j] =max(s[i-1][j], s[i][j-1])
            if s[i][j] == s[i-1][j]:
               backtrack[i][j] = 1
            if s[i][j] == s[i][j-1]:
               backtrack[i][j] = 2 
    #print s==backtrack
    return backtrack
commonseq = []
def OUTPUTLCS(backtrack, v, i, j):
       
        if i == 0 or j == 0:
            return
        if backtrack[i][j] == 1:
            OUTPUTLCS(backtrack, v, i - 1, j)
            commonseq.append('-')
        elif backtrack[i][j] == 2:
            OUTPUTLCS(backtrack, v, i, j - 1)
            commonseq.append('-')
        else:
            OUTPUTLCS(backtrack, v, i - 1, j - 1)  
            commonseq.append(v[i-1])
        return ''.join(commonseq)
#print n, m, down, right
#print LCS(v, w)
v = 'PLEASANTLY'
w = 'MEANLY'
print v
print OUTPUTLCS(LCS(v, w), v, len(v), len(w))