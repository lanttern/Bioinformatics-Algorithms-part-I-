# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:51:16 2013

@author: zhihuixie
"""

def find_clump(genome_small, k, L, t):
    j=0
    #i,n=0,0
    #num=[]
    b=[]
    while j<=len(genome_small)-k:        
        if genome.count(genome_small[j:j+k])>=t and genome_small[j:j+k] not in b:
          b.append(genome_small[j:j+k])
        j+=1
        return b
def find_all(genome, k, L, t):
    #print b
    result=[]
    i=0
    while i<=len(genome)-L:
         temp=find_clump(genome[i:i+L], k, L, t)
            #print item, a
              #print a, genome[j:j+k], i, j
         for item in temp:
             if item not in result:
                 result.append(item)
         i+=1
         print i
    print result, len(result)
            #print i

f=open('E-coli.txt', 'r')
genome=f.read()
genome=genome.translate(None, '\n')
f.close()
k=9
L=500
t=3
find_all(genome, k, L, t)