# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
EXERCISE BREAK: How many DNA strings of length 30 transcribe and translate into Tyrocidine B1?

Recall that the amino acid sequence of Tyrocidine B1 is Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr. We also reproduce the genetic code figure below.
VKLFPWFNQY
@author: zhihuixie
"""
from protein_mRNA_code import genetic_code
code=genetic_code()
protein_seq='VKLFPWFNQY'
num_of_DNA_String=1
for AA in protein_seq:
    num_of_DNA_String*=len(code[AA])
print num_of_DNA_String, len(code['A'])