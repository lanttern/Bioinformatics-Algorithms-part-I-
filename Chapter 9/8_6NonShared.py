# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie
Longest Repeat Problem: Find the longest repeat in a string.
     Input: A string Text.
     Output: A longest repeat in Text, i.e., a longest substring of Text that appears in Text more than once.

CODE CHALLENGE: Solve the Longest Repeat Problem.

Sample Input:
     ATATCGTTTTATCGTT

Sample Output:
     TATCGTT

"""
#from suffix_tree1 import SuffixTree
with open("8_6.txt") as r:
    s = (r.readline()).translate(None, "\n")
    t = (r.readline()).translate(None, "\n")
#s = "CCAAGCTGCTAGAGG" 
#t = "CATGCTGGGCTGGCT"
seed = ["A", "T", "C", "G"]
list1 = seed
Bool = False
def generate_list(l1, l2):
    l3 = []
    for nt1 in l1:
        for nt2 in l2:
              l3.append(nt1 + nt2)
    return l3
while True:
   for el in list1:
       #print el
       if el in s and el not in t:
           Bool = True
           print el
           break
   if Bool:
       break
   else:
       list1 = generate_list(list1, seed)


#print a
#index_sub = set(index_substring)
#print s[index_substring[0]:index_substring[1]]
