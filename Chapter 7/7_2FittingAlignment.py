import sys
import numpy as np
sys.setrecursionlimit(2000)

with open ('7_2.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')

#print v, w
"""
TAGGCTTA
TAGA--TA
"""
#print matrix

#v =  'TCTAGATGAGGGTGCCTTTCGTGTAGCTGATTTCCATGTGGATCACTTATACAGTCCCGGGGGATCGTGTGGGACTTAAAACGAGAATTGGCAGGCCTCAATAGACCCTATGATGAAATGTCACGGGCCGACTGGGATAGGAGGCGACCGACTACTCTAGCGCACACGAACCTGGTTGATTTGATTGGCACACATTCATATCCATGATGTCAGAACGAGACTTGCACAGGTAACGACCACTTAAATAGGTAGATCCAGATCGATCAGCTAATCTGTAACAGCGCAAGTGGCTTCTTGCAGATGGCTCCTGTGTGAAACACAGCGATGATCTCGCATTGACCGCCTTGCAGTGGTGTCCTCTTAACTGAAGCTCGATATCACATCACAGTGTGAGAAAATCCGGGGGCATTGCCTACGTCGCTGATTGTCATTCTTGCAGTGTGATGCAGTCGTGTTGAAGTACGGGGAATATTTGAGTCAAAGTTGGAGGATTCTCAAGAGGTCTGTTCTACGGGCTAGAGCTATCTCATTTCGCTGCCCAGTGGTCAAAGGCGAATCGACTCACTGAAGTAGTTAGGGGAACAGTCCTTCATTTGACATTATGAGGAACCTTAATCTTTGTGCTCTGTATTTCTTCTTCCCAAGGGTATTTCTCATTAGGACATTACGCTAGTACTGTAAACTCCATATAGTGGCGGAATAATCCTGGGCCAGTTATGTGATGCCCTGTCTTGAGATTTGGAAGCGCCTCTTTGCCTCTATTACATATGGCACAGGATACAGCCAAACTGCACGTCGGTTGGTACCCTCCCAACTCCGAGATGTGTTATTGCTAGTTCGGCACGCAGAGATAGAACCTAATATCGCCACATGTGACGAAGCAC'
     
    #seq2 = 'PENALTY'
#w = 'CTACGTAGCCCGTTCGTCATGCCGGGTGAGTTAAGGCGTCCGTAATGGTAGTCTGTTTTTTTGCAAAGTATGGTAACCTAG'
def FIT(v, w):
    n = len(v); m = len(w)
    s = np.zeros((n + 1,m + 1),int)
    s[0][0] = 0
    for i in range(1, n + 1):
        s[i][0] = 0
    for j in range(1, m + 1):
        s[0][j] = -j
    backtrack = np.zeros((n + 1,m + 1),int)
    Best = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #print down[i-1][j], right[i][j-1]
            if v[i-1] == w[j-1]:
               s[i][j] =max(s[i-1][j] - 1, s[i][j-1] - 1, s[i-1][j-1] + 1)
            else:
               s[i][j] =max(s[i-1][j] - 1, s[i][j-1] - 1, s[i-1][j-1] - 1)            
            
            if s[i][j] == s[i][j-1] - 1:
                  backtrack[i][j] = 3
            elif s[i][j] == s[i-1][j] - 1:
                  backtrack[i][j] = 2
            
            elif s[i][j] == s[i-1][j-1] + 1 or s[i][j] == s[i-1][j-1] - 1:
                  backtrack[i][j] = 1
            
    Best = max([s[i][m] for i in range(0, n + 1)])
    for i in range(0, n + 1):
        if Best == s[i][m]:
            Endi = i
            Endj = m
            break
   # Endi = 9
   # Endj = 6
    print Best#, Endi, Endj#, backtrack
    return backtrack, Endi, Endj
seq1 = []
seq2 = []
def OUTPUTFIT(backtrack, v, w, i, j): 
        #print seq1, seq2, i, j, backtrack[i][j]
        if i == 0 or j == 0:
            return
        
        if backtrack[i][j] == 1:
            OUTPUTFIT(backtrack, v, w, i-1, j-1)
            seq1.append(v[i-1])
            seq2.append(w[j-1])    
        elif backtrack[i][j] == 2:
            OUTPUTFIT(backtrack, v, w, i-1, j)
            #print i-1, v[i-1]
            seq1.append(v[i-1])
            seq2.append('-')
        elif backtrack[i][j] == 3:
            OUTPUTFIT(backtrack, v, w, i, j - 1)  
            seq1.append('-')
            seq2.append(w[j-1])
        return ''.join(seq1), ''.join(seq2)
backtrack, i, j = FIT(v,w)
align1, align2 = OUTPUTFIT(backtrack, v, w, i, j)
print align1
print align2
   
