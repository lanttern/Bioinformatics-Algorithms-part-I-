# -*- coding: utf-8 -*-
"""
CODE CHALLENGE: Implement RANDOMIZEDMOTIFSEARCH.

Input: Integers k and t, followed by a collection of strings Dna.

Output: A collection BestMotifs resulting from running RANDOMIZEDMOTIFSEARCH(Dna, k, t) (with pseudocounts) 1000 times.

Sample Input:
     8 5
     CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
     GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
     TAGTACCGAGACCGAAAGAAGTATACAGGCGT
     TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
     AATCCACCAGCTCCACGTGCAATGTTGGCCTA

Sample Output:
     TCTCGGGG
     CCAAGGTG
     TACAGGCG
     TTCAGGTG
     TCCACGTG
@author: zhihuixie
"""
from random import choice
def all_pattern(genome, k):    #function to generate all pattern with k-mer
    pattern=[]
    while k<len(genome):
          pattern.append(genome[0:k])
          genome=genome[1:]  #move to find next seq
    return pattern

def Profile(motifs):
    Nt_pr = {}
    A1,T1,C1,G1 = [], [] , [], []
    for j in range(0, len(motifs[0])):
        A,T,C,G = 1,1,1,1
        for i in range(0, len(motifs)):
            if motifs[i][j] ==  'A':
                A+=1
            if motifs[i][j] == 'T':
                T+=1
            if motifs[i][j] ==  'C':
                C+=1
            if motifs[i][j] == 'G':
                G+=1
       # print A, T, C, G
        A1.append(A*1.0/sum([A,T,C,G]))
        T1.append(T*1.0/sum([A,T,C,G]))
        C1.append(C*1.0/sum([A,T,C,G]))
        G1.append(G*1.0/sum([A,T,C,G]))
    Nt_pr['A'] = A1
    Nt_pr['T'] = T1
    Nt_pr['C'] = C1
    Nt_pr['G'] = G1
    #print motifs, Nt_pr
    return Nt_pr   
   
def Motifs(motifs, allpattern):
    maxpr= 0
    pattern2= []
    Nt_pr1 = Profile(motifs)
    #print Nt_pr1
    for motif1 in allpattern:
        totalpr = 1
        #print motif
        for i in range (0, len(motif1)): 
            temp = Nt_pr1[motif1[i]]
            #print i, motif[i],temp
            totalpr = totalpr * temp[i]
        if totalpr > maxpr:
            maxpr = totalpr
    
    for motif1 in allpattern:
        totalpr = 1
        #print motif
        for i in range (0, len(motif1)): 
            temp = Nt_pr1[motif1[i]]
            #print i, motif[i],temp
            totalpr = totalpr * temp[i]
        if totalpr == maxpr:
            pattern2.append(motif1)
    #print 'pattern2 is: '
    #print pattern2
    return choice(pattern2)
    
def score(motifs):   #function to find pattern with most frequency
    score = 0
   # print motifs
    for i in range(0, len(motifs[0])):
        numA,numT, numC, numG = 0,0,0,0
        for j in range(0, len(motifs)):
            if motifs[j][i] == 'A':
                numA+=1
            if motifs[j][i] == 'T':
                numT+=1
            if motifs[j][i] == 'C':
                numC+=1
            if motifs[j][i] == 'G':
                numG+=1
        #print numA,numT,numC,numG
        score+=sum([numA, numT, numC, numG]) - max([numA, numT, numC, numG])
    #print score
    return score
    
def RandomizedSearch(array, k, t):
    motifs = []
    for dna in array:
        motifs.append(''.join(choice(dna) for x in range(k)))
    bestmotifs = motifs
    #print bestmotifs
    #print firstmotifs
    n = 0
    while True:
        motifs1 = []
        for x in range(0,t):
            allpattern = all_pattern(array[x], k)
            #print x
            motif = Motifs(motifs, allpattern)
            motifs1.append(motif)
        motifs = motifs1
        n+=1
        #print motifs
        if score(motifs)<score(bestmotifs):
            bestmotifs = motifs
        #if score(motifs) >= score(bestmotifs) and n < 3000:
         #   bestmotifs = bestmotifs
        else:
            for element in bestmotifs:
                print element
            print n
            return
   
  
array = []
with open("7_6.txt", "r") as r:
    for line in r:
        array.append(line.translate(None, '\n'))

print array
k = 15
t = 20
#array = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
#k=6
RandomizedSearch(array, k, t)

#print find_pattern(array, 'ATA', num_mismatch)