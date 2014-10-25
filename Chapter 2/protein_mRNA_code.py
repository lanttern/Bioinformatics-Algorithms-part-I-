# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:29:11 2013
Protein to mRNA codes
@author: zhihuixie

"""

def genetic_code():
    code={}
    code['K']=['AAA','AAG']
    code['N']=['AAC','AAU']
    code['T']=['ACA','ACC','ACG','ACU']
    code['R']=['AGA','AGG','CGA','CGC','CGG','CGU']
    code['S']=['AGC','AGU','UCA','UCC','UCG','UCU']
    code['I']=['AUA','AUC','AUU']
    code['M']=['AUG']
    code['Q']=['CAA','CAG']
    code['H']=['CAC','CAU']
    code['P']=['CCA','CCC','CCG','CCU']
    code['L']=['CUA','CUC','CUG','CUU','UUA','UUG']
    code['E']=['GAA','GAG']
    code['D']=['GAC','GAU']
    code['A']=['GCA','GCC','GCG','GCU']
    code['G']=['GGA','GGC','GGG','GGU']
    code['V']=['GUA','GUC','GUG','GUU']
    code['Y']=['UAC','UAU']
    code['C']=['UGC','UGU','UGU','UGC']
    code['W']=['UGG']
    code['F']=['UUC','UUU']
    code['none']=['UAA','UAG','UGA']
    return code
#print genetic_code()