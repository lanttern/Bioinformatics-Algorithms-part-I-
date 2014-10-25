# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
Translation protein sequence from mRNA sequence
@author: zhihuixie
"""
from protein_mRNA_code import genetic_code
def translation(mRNA):
    code=genetic_code()
    Protein=[]
    while 3<=len(mRNA):
        for AA in code:
            #print mRNA[:3]
            if mRNA[:3] in code[AA]:
                if AA!='none':
                   Protein.append(AA)
        mRNA=mRNA[3:]
        #print mRNA
    return ''.join(Protein)