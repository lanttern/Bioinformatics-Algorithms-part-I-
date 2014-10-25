# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:34:01 2013
DNA seq to mRNA
@author: zhihuixie
"""
def DNA_to_mRNA(DNA):
    mRNA=[]
    for nt in DNA:
        if nt=='T':
            nt='U'
        mRNA.append(nt)
    return ''.join(mRNA)
