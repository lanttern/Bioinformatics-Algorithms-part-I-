# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text and an amino acid string Peptide.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).

CODE CHALLENGE: Solve the Peptide Encoding Problem.
@author: zhihuixie
"""
from Protein_translation import translation
from DNA_to_mRNA import DNA_to_mRNA 
from dna_RC import DNA_RC
def peptide_encoding(DNA_seq, peptide):
    mRNA=DNA_to_mRNA(DNA_seq)
    peptide_temp=[]    
    l=len(peptide)*3
    target_DNA=[]
    while l<=len(mRNA):
        peptide_temp=translation(mRNA[:l])
        if peptide_temp==peptide:
            target_DNA.append(DNA_seq[:l])
        mRNA=mRNA[1:]
        DNA_seq=DNA_seq[1:]
    return target_DNA
#DNA_seq='ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
#peptide= 'MA'
f=open('7_2.txt','r')
peptide=f.readline()
peptide=peptide.translate(None,'\n')
DNA_seq=f.read()
DNA_seq=DNA_seq.translate(None,'\n')
f.close()
DNA_seq_RC=DNA_RC(DNA_seq)
for e in peptide_encoding(DNA_seq, peptide):
 print e
for item in peptide_encoding(DNA_seq_RC, peptide):
 print DNA_RC(item)
