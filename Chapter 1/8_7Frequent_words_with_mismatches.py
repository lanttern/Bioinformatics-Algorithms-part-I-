# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:51:16 2013

@author: zhihuixie
Frequent Words with Mismatches Problem (8_7 chapter1)
"""
import itertools
num_mismatch=3
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
total_num=[]
f=open('8_7.txt', 'r')
genome=f.read()
genome=genome.translate(None, '\n')
f.close()
k=8

allpattern=all_pattern(genome, k, num_mismatch)
final_list=[]
n=0
print allpattern
for item in allpattern: # count all pattern num
    total_num.append(find_pattern(genome, item, num_mismatch))
while n<len(total_num): #obtain maxi num
    if total_num[n]==max(total_num):
        final_list.append(allpattern[n])
    n+=1
print final_list

