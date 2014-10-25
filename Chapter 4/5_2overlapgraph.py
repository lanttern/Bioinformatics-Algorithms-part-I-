# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:11:12 2013
You should now be ready to apply your knowledge to solve the Overlap Graph Problem.

CODE CHALLENGE: Solve the Overlap Graph Problem (restated below).
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.

Sample Input:
     ATGCG
     GCATG
     CATGC
     AGGCA
     GGCAT

Sample Output:
     AGGCA -> GGCAT
     CATGC -> ATGCG
     GCATG -> CATGC
     GGCAT -> GCATG
@author: zhihuixie
"""
from Covertdict import Covert
with open ('5_2.txt') as r:
    DNA_array = []
    for line in r:
        line = line.translate(None, '\n')
        DNA_array.append(line)
#print DNA_array
#DNA_array = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT']
def Overlap(DNA_array):
    copy = list(DNA_array)
    pattern = {}
    for DNA in DNA_array:
        for DNAcopy in copy:
            if DNA[1:] == DNAcopy[:-1]:
                pattern[DNA] = DNAcopy
    order_pattern = Covert([item for item in pattern])
    for element in order_pattern:
        print element + ' -> '+ pattern[element]
Overlap(DNA_array)