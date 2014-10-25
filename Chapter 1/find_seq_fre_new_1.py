# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:33:09 2013

@author: zhihuixie
"""

def find_clump(genome, k, L, t, b):
    i=0
    #num=[]
    result=[]

    for item in b:
       while i<=len(genome)-L:
            a=genome[i:L+i].count(item)
              #print a, genome[j:j+k], i, j
            if a>=t and item not in result:
              #num.append(a)
                result.append(item)
            if a in range(t):
                i+=1+(t-a-1)*k
            else:
                i+=1
            
                
       print item
#print n

    print len(result), result
b=[]
f1=open('b.txt', 'r')

for e in f1:
    b.append(e)
f1.close()
f=open('E-coli.txt', 'r')
genome=f.read()
genome=genome.translate(None, '\n')
f.close()
find_clump(genome, 9, 500, 3, 'AAAGGTCTA')