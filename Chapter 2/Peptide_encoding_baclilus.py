# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
EXERCISE BREAK: Solve the Peptide Encoding Problem for Bacillus brevis and Tyrocidine B1 (Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr). How many starting positions in Bacillus brevis encode this peptide? (Genetic code figure reproduced below.)
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
    global i
    i=0.0
    n=len(mRNA)
    while l<=len(mRNA):
        peptide_temp=translation(mRNA[:l])
        i+=1
        print 'Progress percentage: ' + str(i*100/n/2) +'%'
        if peptide_temp==peptide:
            target_DNA.append(DNA_seq[:l])
        mRNA=mRNA[1:]
        DNA_seq=DNA_seq[1:]
    return target_DNA
#DNA_seq='ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
#peptide= 'MA'
f=open('7_2_B.txt','r')
peptide='VKLFPWFNQY'
DNA_seq=f.read()
DNA_seq=DNA_seq.translate(None,'\n')
f.close()
DNA_seq_RC=DNA_RC(DNA_seq)
print len(peptide_encoding(DNA_seq, peptide))+len(peptide_encoding(DNA_seq_RC, peptide))
