# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:51:16 2013

@author: zhihuixie
Frequent Words with Mismatches Problem (8_7 chapter1)
"""
import itertools
num_mismatch=2
new_list = [''.join(item) for item in itertools.product('ATCG', repeat=num_mismatch)]
def all_pattern(genome, k, num_mismatch):    #function to generate all pattern with k-mer
    pattern=[]
    allpattern1=[]
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
def find_pattern(genome, pattern, num_mismatch):   #function to find pattern with most frequency
    l=len(pattern)
    num=0
    while l<len(genome):
      i=0
      count=0
      while i<l:
          if pattern[i]==genome[i]:
              count+=1          # count matched bases
          i+=1
      if count>=l-num_mismatch: # add all mis matched seq
         num+=1
      genome=genome[1:]  #move to find next seq
    return num
def reverse_c(seq): #function to generate reverse complementary sequence
    seq1=[]
    j=0
    for i in seq:
        seq1.append(i)
    while j<len(seq1):
       if seq1[j]=='A':
        seq1[j]='B'
       if seq1[j]=='T':
        seq1[j]='A'
       if seq1[j]=='B':
        seq1[j]='T'
       if seq1[j]=='C':
        seq1[j]='D'
       if seq1[j]=='G':
        seq1[j]='C'
       if seq1[j]=='D':
        seq1[j]='G'
       j+=1
    seq1.reverse()
    return ''.join(seq1)

total_num=[]
f=open('8_8.txt', 'r')
genome=f.read()
genome=genome.translate(None, '\n')
f.close()
k=8
allpattern=all_pattern(genome, k, num_mismatch)
allpatternRC=[]
final_list=[]
total_numRC=[]
alltotalnum=[]
n, m=0, 0
for element in allpattern: # generate reverse complementary pattern
    new_element=reverse_c(element)
    if new_element not in allpatternRC:
       allpatternRC.append(new_element) # total pattern

for item in allpattern: # count all pattern num
    total_num.append(find_pattern(genome, item, num_mismatch))
for itemRC in allpatternRC: # count all pattern num
    total_numRC.append(find_pattern(genome, itemRC, num_mismatch))
    
while m<len(total_num): #obtain maxi num
    alltotalnum.append(total_num[m]+total_numRC[m])
    m+=1
while n<len(alltotalnum):
    if alltotalnum[n]==max(alltotalnum):
        a=allpattern[n]
        b=allpatternRC[n]
        if a not in final_list:
           final_list.append(a)
        if b not in final_list:
           final_list.append(b)
    n+=1
print final_list

