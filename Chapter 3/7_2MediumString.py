# -*- coding: utf-8 -*-
"""
We now give the pseudocode for a brute force solution to the Median String Problem.

    MEDIANSTRING(Dna, k)
        BestPattern ← AAA…AA
        for each k-mer Pattern from AAA…AA to TTT…TT
            if d(Pattern, Dna) < d(BestPattern, Dna)
                 BestPattern ← Pattern
        output BestPattern

CODE CHALLENGE: Implement MEDIANSTRING.
     Input: An integer k, followed by a collection of strings Dna.
     Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern.

Sample Input:
     3
     AAATTGACGCAT
     GACGACCACGTT
     CGTCAGCGCCTG
     GCTGAGCACCGG
     AGTACGGGACAG

Sample Output:
     GAC
@author: zhihuixie
"""
import itertools
def all_pattern(array, k, num_mismatch):    #function to generate all pattern with k-mer
    pattern=[]
    allpattern1=[]
    for genome in array:
        while k-num_mismatch<len(genome):
          pattern.append(genome[0:k-num_mismatch])
          genome=genome[1:]  #move to find next seq
    for item2 in pattern:
        i=0
        while i<=len(item2):
            for e in new_list:
                temp=item2[:i]+e+item2[i:]
                if temp not in allpattern1:
                    allpattern1.append(temp)
            i+=1
    return allpattern1
def distance_of_pattern(array, pattern):   #function to find pattern with most frequency
    l=len(pattern)
    total = []
    for genome in array:
       num=[]
       while l<=len(genome):
         i=0
         count=0
         while i<l:
            if pattern[i]!=genome[i]:
               count+=1          # count matched bases
            i+=1
         num.append(count)
         genome=genome[1:]  #move to find next seq
         #print num
       total.append(min(num))
    #print total
    return sum(total)
def MotifEnumeration(array, k, num_mismatch):
   allpattern=all_pattern(array, k, num_mismatch)
   best_pattern = allpattern[0]
   #print allpattern
   #print '\n'
   for item in allpattern: # count all pattern num
      if distance_of_pattern(array, item) < distance_of_pattern(array, best_pattern):
          best_pattern = item
   print best_pattern
  
array = []
with open("7_2.txt", "r") as r:
    for line in r:
        array.append(line.translate(None, '\n'))
print array

#array = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
k=6
num_mismatch=0
new_list = [''.join(item) for item in itertools.product('ATCG', repeat=num_mismatch)]
MotifEnumeration(array, k, num_mismatch)
#print find_pattern(array, 'ATA', num_mismatch)