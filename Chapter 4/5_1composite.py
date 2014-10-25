# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:29:40 2013
CODE CHALLENGE: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text), where the k-mers are written in lexicographic order.

Sample Input:
     5
     CAATCCAAC

Sample Output:
     AATCC
     ATCCA
     CAATC
     CCAAC
     TCCAA
@author: zhihuixie
"""
#import sys
#sys.setrecursionlimit(10000)
with open('5_1.txt') as r:
    k = int((r.readline()).translate(None, '\n'))
    genome = (r.readline()).translate(None, '\n')
print k#, genome
#k = 5
#genome = 'CAATCCAAC'
#dnastring = [genome[0:k]]
def Substring(k, genome):
    s = []
    while k <= len(genome):
        s.append(genome[0:k])
        genome = genome[1:]
    return s
'''
    if len(genome) == k:
        return [genome]
    if len(genome) < k:
        return []
    return [genome[0:k]] + Substring(k, genome[1:])
'''        
#print Substring(k, genome)
def Composition(k, genome):
    Nt = {'A':'0', 'C':'1', 'G':'2','T':'3'}
    substring = {}
    dnastring = Substring(k, genome)
    for element in dnastring:
        convert= int(''.join([Nt[key] for key in element]))
        substring[convert]=element
    order_of_string = sort([i for i in substring])
    for item in order_of_string:
        print substring[item]
Composition(k, genome)        