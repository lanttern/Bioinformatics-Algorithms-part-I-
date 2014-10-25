# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).

CODE CHALLENGE: Solve the Generating Theoretical Spectrum Problem.

Sample Input:
     LEQN

Sample Output:
     0 113 114 128 129 227 242 242 257 355 356 370 371 484
"""
from mass import mass_of_AA
def sub_peptide(peptide): # generate all subpeptides
    l=1 #length of subpeptide
    subpeptide=[]
    while l<len(peptide):
     i=0
     while i<=len(peptide)-l:
        subpeptide.append(peptide[i:i+l])
        i+=1
     while len(peptide)-l<i<len(peptide):     
       subpeptide.append(peptide[i:]+peptide[:(l+i-len(peptide))])
       i+=1
     l+=1
    subpeptide.append(peptide)
    return subpeptide
def masssubpeptides(peptide): # calculate mass of subpeptides
    subpeptides=sub_peptide(peptide)
    masssubpeptide=[0]
    for item in subpeptides: 
        Sum=0
        for AA in item:
            temp = mass_of_AA()
            Sum = Sum + temp[AA]
        masssubpeptide.append(Sum)
    return masssubpeptide