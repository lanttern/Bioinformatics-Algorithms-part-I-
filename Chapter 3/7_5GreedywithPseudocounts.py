# -*- coding: utf-8 -*-
"""
Now that you have seen GREEDYMOTIFSEARCH perform well on a sample dataset, update your GREEDYMOTIFSEARCH implementation to incorporate pseudocounts.

CODE CHALLENGE: Implement GREEDYMOTIFSEARCH with pseudocounts.
     Input: Integers k and t, followed by a collection of strings Dna.
     Output: A collection of strings BestMotifs resulting from applying GREEDYMOTIFSEARCH(Dna,k,t) with
     pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string,
     use the one occurring first.

Sample Input:
     3 5
     GGCGTTCAGGCA
     AAGAATCAGTCA
     CAAGGAGTTCGC
     CACGTCAATCAC
     CAATAATATTCG

Sample Output:
     TTC
     ATC
     TTC
     ATC
     TTC
@author: zhihuixie
"""
#import itertools
def all_pattern(genome, k):    #function to generate all pattern with k-mer
    pattern=[]
    while k<len(genome):
          pattern.append(genome[0:k])
          genome=genome[1:]  #move to find next seq
    return pattern

def matrix(motifs):
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
   
def Profile_most(motifs, allpattern):
    maxpr= 0
    pattern2= []
    Nt_pr1 = matrix(motifs)
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
    return pattern2[0]
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
    
def GreedySearchP(array, k, t):
    firstmotifs = all_pattern(array[0], k)
    #print bestpattern, bestmotif
    #print firstmotifs
    motifs_total = []
    for n in range(0, len(firstmotifs)):
        #print firstmotifs[n]
        motifs = [firstmotifs[n]]
        for x in range(1,t):
            allpattern = all_pattern(array[x], k)
            #print x
            allmotifs = Profile_most(motifs, allpattern)
            motifs.append(allmotifs)
            #print motifs
        motifs_total.append(motifs)
    #print motifs_total
    bestmotifs = motifs_total[0]
    for motifs1 in motifs_total:
        if score(motifs1)<score(bestmotifs):
            bestmotifs = motifs1
    for element in bestmotifs:
        print element        
   
  
array = []
with open("7_5.txt", "r") as r:
    for line in r:
        array.append(line.translate(None, '\n'))

print array
k = 12
t = 25
#array = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
#k=6
GreedySearchP(array, k, t)

#print find_pattern(array, 'ATA', num_mismatch)