# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:30:20 2013
CODE CHALLENGE: Solve the De Bruijn Graph from a String Problem.
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text).

Sample Input:
     4
     AAGATTCTCTAC

Sample Output:
     AAG -> AGA
     AGA -> GAT
     ATT -> TTC
     CTA -> TAC
     CTC -> TCT
     GAT -> ATT
     TCT -> CTA,CTC
     TTC -> TCT

Extra Dataset
@author: zhihuixie
"""
from Covertdict import Covert
with open('5_3.txt') as r:
    k = int((r.readline()).translate(None, '\n'))
    genome = (r.readline()).translate(None, '\n')
print k#, genome

#k = 4
#genome = 'AAGATTCTCTAC'
#dnastring = [genome[0:k]]
def Substring(k, genome):
    s = []
    while k-1 <= len(genome):
        if genome[0:k-1] not in s:
           s.append(genome[0:k-1])
        genome = genome[1:]
    return s
def DeBruijn(DNA_array):
    copy = list(DNA_array)
    pattern = {}
    for DNA in DNA_array:
        temp = []
        for DNAcopy in copy:
            if DNA[1:] == DNAcopy[:-1] and DNA + DNAcopy[-1] in genome:
                temp.append(DNAcopy)
                pattern[DNA] = temp
    #print pattern
    order_pattern = Covert([item for item in pattern])
    for element in order_pattern:
        print element + ' -> '+ str(pattern[element])
DNA_array = Substring(k, genome)
DeBruijn(DNA_array)