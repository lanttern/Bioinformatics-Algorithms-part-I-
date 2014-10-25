from sys import *
import numpy as np
from Bio.SubsMat import MatrixInfo as matlist 

with open ('7_6.txt') as r:
    v = (r.readline()).translate(None, '\n')
    w = (r.readline()).translate(None, '\n')
#print v, w
#v = 'PLEASANTLY'
#w = 'MEANLY'
similarityMatrixMap = matlist.blosum62
def computeFMatrix(seq1, seq2, gap):
    '''This function creates alignment score matrix
    seq1 : reference sequence
    seq2 : other sequence
    gap : gap penalty '''
 
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    fMatrix = np.zeros((rows,cols),float)
    
    for i in range(0, rows):
        fMatrix[i][0] = i * gap
 
    for j in range(0, cols):
        fMatrix[0][j] = j * gap
 
    for i in range(1, rows):
        for j in range(1, cols):
            if (seq1[i - 1], seq2[j - 1]) in similarityMatrixMap:
               mtch = fMatrix[i - 1][j - 1] + similarityMatrixMap[(seq1[i - 1], seq2[j - 1])]
            elif (seq2[j - 1], seq1[i - 1]) in similarityMatrixMap:
                mtch = fMatrix[i - 1][j - 1] + similarityMatrixMap[(seq2[j - 1], seq1[i - 1])]
            delete = fMatrix[i - 1][j] + gap
            insert = fMatrix[i][j - 1] + gap
            fMatrix[i][j] = max(mtch, delete, insert)
 
    return trackBack(fMatrix, seq1, seq2, gap, similarityMatrixMap), fMatrix[-1][-1]
 
def trackBack(fMatrix, seq1, seq2, gap, similarityMap):
    '''Tracks back to create the aligned sequence pair'''
    alignedSeq1 = ''
    alignedSeq2 = ''
    i = len(seq1)
    j = len(seq2)
    while i > 0 and j > 0:
        score = fMatrix[i][j]
        diagScore = fMatrix[i - 1][j - 1]
        upScore = fMatrix[i][j - 1]
        leftScore = fMatrix[i -1][j]
        if (seq1[i - 1], seq2[j - 1]) in similarityMatrixMap:
          if score == diagScore + similarityMap[(seq1[i - 1], seq2[j - 1])]:
            alignedSeq1 = seq1[i - 1] + alignedSeq1
            alignedSeq2 = seq2[j - 1] + alignedSeq2
            i -= 1
            j -= 1
        
          elif score == leftScore + gap:
            alignedSeq1 = seq1[i - 1] + alignedSeq1
            alignedSeq2 = '-' + alignedSeq2
            i -= 1
          elif score == upScore + gap:
            alignedSeq1 = '-' + alignedSeq1
            alignedSeq2 = seq2[j - 1] + alignedSeq2
            j -= 1
          else:
            stderr.write('Not Possible')
        elif (seq2[j - 1], seq1[i - 1]) in similarityMatrixMap:
          if score == diagScore + similarityMap[(seq2[j - 1], seq1[i - 1])]:
            alignedSeq1 = seq1[i - 1] + alignedSeq1
            alignedSeq2 = seq2[j - 1] + alignedSeq2
            i -= 1
            j -= 1
        
          elif score == leftScore + gap:
            alignedSeq1 = seq1[i - 1] + alignedSeq1
            alignedSeq2 = '-' + alignedSeq2
            i -= 1
          elif score == upScore + gap:
            alignedSeq1 = '-' + alignedSeq1
            alignedSeq2 = seq2[j - 1] + alignedSeq2
            j -= 1
          else:
            stderr.write('Not Possible')
    while i > 0:
        alignedSeq1 = seq1[i - 1] + alignedSeq1
        alignedSeq2 = '-' + alignedSeq2
        i -= 1
 
    while j > 0:
        alignedSeq1 = '-' + alignedSeq1
        alignedSeq2 = seq2[j - 1] + alignedSeq2
        j -= 1
 
    return (alignedSeq1, alignedSeq2)
 
if __name__ == "__main__":
    seq1 = v
    seq2 = w
    #seq1 = 'PLEASANTLY'
    #seq2 = 'MEANLY'
 
    (alignedSeq1, alignedSeq2), score = computeFMatrix(seq1, seq2, -5)
    print int(score)    
    print alignedSeq1
    print alignedSeq2
