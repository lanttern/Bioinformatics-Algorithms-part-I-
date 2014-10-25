# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
We now have the outline for an algorithm. Given an experimental spectrum, we first compute the convolution of an experimental spectrum. We then select the M most frequent elements between 57 and 200 to form a putative alphabet of amino acid masses; in order to be fair, we should include the top M elements of the convolution “with ties”. Finally, we run the algorithm LEADERBOARDCYCLOPEPTIDESEQUENCING, where the amino acid masses are restricted to this alphabet. We call this algorithm CONVOLUTIONCYCLOPEPTIDESEQUENCING.

CODE CHALLENGE: Implement CONVOLUTIONCYCLOPEPTIDESEQUENCING.

Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.

Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

Sample Input:
     20
     60
     57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493

Sample Output:
     99-71-137-57-72-57
"""
from mass import mass_of_AA
#import itertools
#from product import gen_list
#from masssubp import masssubpeptides
temp = mass_of_AA ()
mass_AA = []
for AA in temp:
    mass_AA.append(temp[AA])
mass_AA.pop()
'''
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
'''
from heapq import nlargest
from collections import Counter
#import itertools
#from product import gen_list
#from masssubp import masssubpeptides

f = open('7_7E.txt', 'r')
Spectrum1 = f.read()
f.close
#print Spectrum1
Spectrum1 = Spectrum1.translate(None, '\n')
Spectrum1 = Spectrum1.split()
Spectrum = []
for num in Spectrum1:
    Spectrum.append(int(num)) 
counter = dict(Counter(Spectrum)) 

#print Spectrum[-1], type(Spectrum[0])
#Spectrum = [0, 137, 186, 323]    
#Spectrum = [0,71,113,115,129,131,137,147,156,163,186,227,244,244,250,257,262,284,292,317,319,381,388,390,391,397,399,407,413,430,448,501,512,519,528,528,544,554,563,567,576,634,638,641,643,657,691,705,707,710,714,772,781,785,794,804,820,820,829,836,847,900,918,935,941,949,951,957,958,960,967,1029,1031,1056,1064,1086,1091,1098,1104,1104,1121,1162,1185,1192,1201,1211,1217,1219,1233,1235,1277,1348]

def Spectral_Convolution (M, Spectrum):
    list1=[]
    final_list = {}
    for i in range(0, len(Spectrum)):
        for j in range (0, len(Spectrum)-1):
            if Spectrum[i] > Spectrum[j] and 57<=Spectrum[i]-Spectrum[j]<=200:
                list1.append(Spectrum[i]-Spectrum[j])
                
    #print count2
    counter2 = dict(Counter(list1)) 
    #print counter1
    count1 = nlargest(M,[counter2[v] for v in counter2])
    for key in counter2:
       if counter2[key] in count1:
           final_list[str(key)] = key
    #final_list.sort()
    return final_list
    
def submass(peptide):
    peptide = peptide.split()
    #print peptide
    intpeptide = []
    for num in peptide:
        intpeptide.append(int(num))
    
    l=1 #length of subpeptide
    subpeptide=[]
    while l<len(intpeptide):
     i=0
     #Sum=0
     while i<=len(intpeptide)-l:
         subpeptide.append(sum(intpeptide[i:i+l]))
         i+=1
     while len(intpeptide)-l<i<len(intpeptide):     
       subpeptide.append(sum(intpeptide[i:]+intpeptide[:(l+i-len(peptide))]))
       i+=1
     l+=1
    subpeptide.append(sum(intpeptide)) 
    return subpeptide

def gen_list(a, b): # function to grow list
    List = {}
    #newlist = {}
    for i in a:
      for j in b:
        List[i + ' ' + j] =submass(i + ' ' + j)
    return List

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
    
def CYCLOPEPTIDESEQUENCING(M, N, Spectrum):
    seed = Spectral_Convolution (M, Spectrum)
    List = seed #seed    
    list1={}
    while List:
        List = gen_list(List, seed)
        
        #score3 = []
        score3 = [score(List[peptide]) for peptide in List]
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
                if Mass[-1] > max(Spectrum):
                    del List[peptide]
                if Mass[-1] == max(Spectrum):
                    list1[peptide] = List[peptide]
                    del List[peptide]
            j+=1
            
    #print list1, max(Spectrum)
    list2 = []
    score5 = [score(list1[peptide]) for peptide in list1]
    for item in list1:
        if score(list1[item]) in nlargest(23, score5):#== max(score5):
           item = item.split()
           list2.append( '-'.join(item))
    print list2
M = 20
N = 1000
CYCLOPEPTIDESEQUENCING(M,N, Spectrum)
#print Spectral_Convolution (M, Spectrum)
                