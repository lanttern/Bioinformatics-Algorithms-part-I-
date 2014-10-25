# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:24:43 2013

@author: zhihuixie
"""
def Covert(dnastring):
    substring = {}
    Nt = {'A':'0', 'C':'1', 'G':'2','T':'3'}
    num = []
    l = max([len(el) for el in dnastring]) + 1
    for element in dnastring:
        convert= int(''.join([Nt[key] for key in element]))
        c = convert*(10**(l-len(element)))
        num.append(c)
        substring[c] = element
    num.sort()
    return [substring[item] for item in num] 
#print Covert(['GCATG', 'CATGC', 'AGGCA', 'GGCAT', 'AGGCA', 'T', 'CC','TC'])