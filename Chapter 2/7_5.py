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
import itertools
#from product import gen_list
#from masssubp import masssubpeptides
temp = mass_of_AA ()
mass_AA = []
for AA in temp:
    mass_AA.append(temp[AA])
mass_AA.pop()
"""
def gen_list(a, b): # function to grow list
    List=[]
    for i in range(0,len(a)):
        for j in range(0, len(b)):
            if a[i] + b[j] not in List:
               List.append(a[i] + b[j])
            if b[j] + a[i] not in List:
               List.append(b[j] + a[i])
    return List
"""
def CYCLOPEPTIDESEQUENCING(Spectrum):
    seed , a= [], []
    Spectrum.sort()
    for element in Spectrum:
        if element in mass_AA:
            a.append(element)
        for AA in temp:
          if temp[AA] == element and AA != 'none':
             seed.append(AA)
    seed=set(seed)
    List = seed #seed    
    i = 0   
    #seed = str(seed)
    print a, sum(a), len(a), seed, len(seed), List
#Spectrum = [0,71,99,103,113,113,114,114,128,137,184,185,202,212,227,228,240,241,265,298,299,312,315,326,339,341,368,378,412,412,426,429,440,449,452,467,481,511,525,540,543,552,563,566,580,580,614,624,651,653,666,677,680,693,694,727,751,752,764,765,780,790,807,808,855,864,878,878,879,879,889,893,921,992]
#CYCLOPEPTIDESEQUENCING(Spectrum)

    while i < len(a)-1:
        List = map(''.join, itertools.chain(itertools.product(List, seed), itertools.product(seed, List)))
        new_list = []
        for peptide in List:           
            mass = mass_of_peptide(peptide) #masssubpeptides(peptide)
             #mass not in Spectrum
            #mass.sort()
            #print mass, peptide
            if mass in Spectrum and peptide not in new_list:
                new_list.append(peptide)
                print mass, peptide
        List = new_list
        i+=1
    return List

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
    
def mass_of_peptide(peptide): # function to calculate mass of peptide
    Sum = 0
    for AA in peptide:
        Sum+=temp[AA]
    return Sum
        
    
def peptide_to_mass(peptide): # translate peptide seq to mass
    mass = []
    for AA in peptide:
        mass.append(temp[AA])
    return mass
#Spectrum = [0,113,128,186,241,299,314,427]
Spectrum = [0,71,99,103,113,113,114,114,128,137,184,185,202,212,227,228,240,241,265,298,299,312,315,326,339,341,368,378,412,412,426,429,440,449,452,467,481,511,525,540,543,552,563,566,580,580,614,624,651,653,666,677,680,693,694,727,751,752,764,765,780,790,807,808,855,864,878,878,879,879,889,893,921,992]

subpeptides = CYCLOPEPTIDESEQUENCING(Spectrum)
#print subpeptides
final_result=[]
for p in subpeptides:
    if peptide_to_mass(p) not in final_result:
        final_result.append(peptide_to_mass(p))
print final_result, len(final_result)
