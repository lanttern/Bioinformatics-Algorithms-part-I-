# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
ODE CHALLENGE: Implement CYCLOPEPTIDESEQUENCING (pseudocode reproduced below).

Note: After the failure of the first brute-force algorithm we considered, you may be hesitant to implement this algorithm for fear that it will take a long time to run. The potential problem with CYCLOPEPTIDESEQUENCING is that it may generate incorrect k-mers at intermediate stages (i.e., k-mers that are not subpeptides of a correct solution). You may wish to wait to implement CYCLOPEPTIDESEQUENCING until after the next section, where we will analyze this algorithm.

    CYCLOPEPTIDESEQUENCING(Spectrum)
        List ← {0-peptide}
        while List is nonempty
            List ← Expand(List)
            for each peptide Peptide in List
                if Cyclospectrum(Peptide) = Spectrum
                    output Peptide
                    remove Peptide from List
                else if Peptide is not consistent with Spectrum
                    remove Peptide from List

Sample Input:
     0 113 128 186 241 299 314 427

Sample Output:
     186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
"""
from heapq import nlargest
from mass import mass_of_AA
from collections import Counter
#import itertools
#from product import gen_list
#from masssubp import masssubpeptides
temp = mass_of_AA ()

f = open('7_7.txt', 'r')
Spectrum1 = f.read()
f.close
#print Spectrum1
Spectrum1 = Spectrum1.translate(None, '\n')
Spectrum1 = Spectrum1.split()
Spectrum = []
N=180
for num in Spectrum1:
    Spectrum.append(int(num))    
#print Spectrum[-1], type(Spectrum[0])
#Spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]    
#Spectrum = [0,71,113,115,129,131,137,147,156,163,186,227,244,244,250,257,262,284,292,317,319,381,388,390,391,397,399,407,413,430,448,501,512,519,528,528,544,554,563,567,576,634,638,641,643,657,691,705,707,710,714,772,781,785,794,804,820,820,829,836,847,900,918,935,941,949,951,957,958,960,967,1029,1031,1056,1064,1086,1091,1098,1104,1104,1121,1162,1185,1192,1201,1211,1217,1219,1233,1235,1277,1348]
counter = dict(Counter(Spectrum))
seed = {}
length = 0
for element in Spectrum:
    for AA in temp:
      if element == temp[AA]:
         seed[AA] = element
         length+=1
print seed, length
def submass(peptide):
    intpeptide = []
    #print peptide
    for AA in peptide:
        intpeptide.append(temp[AA])
    
    l=1 #length of subpeptide
    #subpeptide={}
    subpeptide1 = [0]
    while l<len(intpeptide):
     i=0
     #Sum=0
     
     while i<=len(intpeptide)-l:
         #if str(intpeptide[i:i+l]) not in subpeptide:
            #subpeptide[str(intpeptide[i:i+l])] = sum(intpeptide[i:i+l])
         #print subpeptide
         subpeptide1.append(sum(intpeptide[i:i+l]))#subpeptide[str(intpeptide[i:i+l])])
         i+=1
     
     while len(intpeptide)-l<i<len(intpeptide): 
       #if str(intpeptide[i:]+intpeptide[:(l+i-len(peptide))]) not in subpeptide:
           #subpeptide[str(intpeptide[i:]+intpeptide[:(l+i-len(peptide))])] = sum(intpeptide[i:]+intpeptide[:(l+i-len(peptide))])
       subpeptide1.append(sum(intpeptide[i:]+intpeptide[:(l+i-len(peptide))]))#subpeptide[str(intpeptide[i:]+intpeptide[:(l+i-len(peptide))])])
       i+=1
     
     
     l+=1
    #if str(intpeptide) not in subpeptide:
     #   subpeptide[str(intpeptide)] = sum(intpeptide)
    subpeptide1.append(sum(intpeptide))#subpeptide[str(intpeptide)])
    
    #print subpeptide[str([156, 71])]
    return subpeptide1

def is_circle(s1, List):
    for item in List:
        if len(s1) == len(item) and s1 in item*2:
           return True
    return False

def gen_list(a, b): # function to grow list
    list1 = {}
    for i in a:
      for j in b:
          #if not is_circle(i+j, list1): 
             list1[i+j] = submass(i+j)
             #list1[j+i] = submass(i+j)
             #list1[j+i]=submass(j+i)
    return list1

def score(peptidemass):
    score1 = 0
    counter1= dict(Counter(peptidemass))
    for el in counter1:
        if el in counter:
            if counter[el] > counter1[el]:
               score1+=counter1[el]
            else:
                score1+=counter[el]
    return score1
    
def CYCLOPEPTIDESEQUENCING(Spectrum):
    List = seed #seed    
    #i = 0   
    list1 = {}
    #print length, seed,len(seed), type(list1)
    #seed = str(seed)
    #print a, sum(a), len(a)
    while List:
        List = gen_list(List, seed)
        
        
        #score3 = []
        score3 = [score(List[peptide]) for peptide in List ]
           #print score3#, submass(peptide)
        score4 = list(score3)
        score6 = nlargest(N, score3)
        #score3 = list (score3)
        j = 0
        print len(score4), max(score4), min(score6)#, len(List), score6
        for peptide in List.keys():  
            if score4[j] not in score6:
                 del List[peptide]
            else:
                #print AA_to_mass(peptide)
                Mass = List[peptide]
                if Mass[-1] > Spectrum[-1]:
                    del List[peptide]
                if Mass[-1] == Spectrum[-1]:
                    list1[peptide] = List[peptide]
                    del List[peptide]
            j+=1
            
        #i+=1
            #len(List), j
    #print List

    score5 = [score(list1[peptide]) for peptide in list1]
    for item in list1:
        if score(list1[item]) == 736:
            print AA_to_mass(item)
            print '\n'
        if score(list1[item]) == max(score5):
           print AA_to_mass(item),max(score5)
           
def AA_to_mass(peptide):
    mass_p = ''
    for AA in peptide:
        mass_p+=str(temp[AA]) + '-'
    return mass_p

CYCLOPEPTIDESEQUENCING(Spectrum)
#print score(submass('156 71 113 114 131 156 113 101 129 128 128 114 128 103 97 131 131 113 131 113 128 115 128 113'))