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

f = open('7_5.txt', 'r')
Spectrum1 = f.read()
f.close
#print Spectrum1
Spectrum1 = Spectrum1.translate(None, '\n')
Spectrum1 = Spectrum1.split()
Spectrum = []
for num in Spectrum1:
    Spectrum.append(int(num))    
#print Spectrum[-1], type(Spectrum[0])
#Spectrum = [0,113,128,186,241,299,314,427]    
#Spectrum = [0,71,113,115,129,131,137,147,156,163,186,227,244,244,250,257,262,284,292,317,319,381,388,390,391,397,399,407,413,430,448,501,512,519,528,528,544,554,563,567,576,634,638,641,643,657,691,705,707,710,714,772,781,785,794,804,820,820,829,836,847,900,918,935,941,949,951,957,958,960,967,1029,1031,1056,1064,1086,1091,1098,1104,1104,1121,1162,1185,1192,1201,1211,1217,1219,1233,1235,1277,1348]
seed = {}
count={}
Spectrum.sort()
length = 0
mass = []
for element in Spectrum:
    if element in mass_AA:
       count[str(element)] = Spectrum.count(element)
       seed[str(element)] = element
       length+=1
       mass.append(element)

def gen_list(a, b): # function to grow list
    List = {}
    newlist = {}
    for i in a:
      for j in b:
       if i + ' ' + j not in List:
        List[i + ' ' + j] =a[i] + b[j]
       if i + ' ' + j not in List:
        List[j + ' ' + i] = a[i] + b[j]
    for e in List:
        temp = e.split()
        count_temp = 0
        for AA in count:
            if temp.count(AA) > count [AA]:
                count_temp+= 1
        if count_temp == 0:
           newlist[e] = List[e]
    return newlist

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
    
def CYCLOPEPTIDESEQUENCING(Spectrum):
    list1 = seed #seed    
    i = 0   
    #print length, seed,len(seed), type(list1)
    #seed = str(seed)
    #print a, sum(a), len(a)
    while list1:#i < length - 1:
        List = gen_list(list1, seed)
        new_list = {}
        final_list=[]
        for peptide in List:  
            if List[peptide] in Spectrum: #and peptide not in new_list:
                new_list[peptide] = List[peptide]
                if List[peptide] == Spectrum[-1]:
                    peptidemass = submass(peptide)
                    peptidemass.sort()
                    #print peptidemass
                    if peptidemass == Spectrum[1:]:
                        print peptide, type(peptide)
                        #peptide = ' '.join(peptide)
                        #peptide = peptide.replace(' ', '-')
                        final_list.append(peptide) #List[peptide], peptide
        #print new_list
        list1 = new_list
        i+=1
    print final_list, len(final_list)
'''
    for item in list1:
        print list1[item], item
    print len(list1)
'''
CYCLOPEPTIDESEQUENCING(Spectrum)
