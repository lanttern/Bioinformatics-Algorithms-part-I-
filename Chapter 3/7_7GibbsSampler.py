# -*- coding: utf-8 -*-
"""
CODE CHALLENGE: Implement GIBBSSAMPLER.
     Input: Integers k, t, and N, followed by a collection of strings Dna.
     Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with pseudocounts and 
     20 random starts.

Sample Input:
     8 5 100
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
from random import randint
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
   
def Random_motifs(motifs1, allpattern):
    Nt_pr1 = Profile(motifs1)
    #print Nt_pr1
    pr = {}
    for motif1 in allpattern:
        totalpr = 1
        #print motif
        for i in range (0, len(motif1)): 
            temp = Nt_pr1[motif1[i]]
            #print i, motif[i],temp
            totalpr = totalpr * temp[i]
        pr[motif1] = totalpr  
    #print pr, len(pr)
    maxpr = max([pr[key] for key in pr])
    
    #pattern2 = choice(pr)
    #print 'pattern2 is: '
    #print pattern2
    return choice([motif for motif in pr if pr[motif] == maxpr])
    
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
    
def GibbsSearch(array, k, t, N):
    motifs = []
    for dna in array:
        motifs.append(''.join(choice(dna) for x in range(k)))
    bestmotifs = motifs
    #print bestmotifs
    #print firstmotifs
    j = 0
    while j < N:
        i = randint(0, t-1)
        allpattern = all_pattern(array[i], k)
            #print x
        #print 'this is: '
        #print motifs, motifs[:i] + motifs[i+1:]
        motif = Random_motifs(motifs[:i] + motifs[i+1:], allpattern)
        motifs[i] = motif
        #print motifs
        if score(motifs)<score(bestmotifs):
            bestmotifs = motifs
        j+=1
        #print j
        #if score(motifs) >= score(bestmotifs) and n < 3000:
         #   bestmotifs = bestmotifs
    print score(bestmotifs)    
    for element in bestmotifs:
        print element
   
  
array = []
with open("7_7.txt", "r") as r:
    for line in r:
        array.append(line.translate(None, '\n'))

print array
k = 15
t = 20
N = 2000
#array = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
#k=6
GibbsSearch(array, k, t, N)
print score(['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG'])

#print find_pattern(array, 'ATA', num_mismatch)