# -*- coding: utf-8 -*-
"""
Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).
     Input: A collection of k-mers Patterns.
     Output: All contigs in DeBruijn(Patterns).

CODE CHALLENGE: Solve the Contig Generation Problem.

Sample Input:
     ATG
     ATG
     TGT
     TGG
     CAT
     GGA
     GAT
     AGA

Sample Output:
     AGA ATG ATG CAT GAT TGGA TGT

@author: zhihuixie
"""
from Covertdict import Covert
with open('5_5.txt') as r:
    array = []
    for line in r:
        s = line.translate(None, '\n')
        array.append(s)
    
def Graph(array):
    graph = {}  
    a1 = list(array)
    for string in array:
        temp = []
        for s1 in a1:
            if string[:-1] == s1[:-1]:
                temp.append(s1[1:])
        graph[string[:-1]] = temp
    return graph
    
G = Graph(array)

def ContigGeneration(G1): 
   allvalues = []
   for el in G1.values ():
        for item in el:
            allvalues.append(item)
   #c = Counter(G1.values())
   nodes = [n for n in G1 if not len(G1[n]) == allvalues.count(n)== 1] 
   allpath = []
   for node in nodes:
     i = 0
     while i < len(G1[node]):
       #print node
       path = []
       while True:
        #   print i
           if i >= len(G1[node]):
              v = G1[node][-1] 
           else:
              v = G1[node][i]
           path.append((node, v))
           c = allvalues.count(v)
           #print v, c
           if v not in G1 or len(G1[v]) > 1 or c > 1:
               break
           else:
               node = v
       i += 1    
       allpath.append(path)    
    
   #print allpath
   contigs = []
   for element in allpath:
        if len(element) == 1:
            contigs.append(element[0][0] + element[0][-1][-1])
        else:
            contig = element[0][0]+ element[0][-1][-1]
            for i in range(1, len(element)):
                contig += element[i][-1][-1]
            contigs.append(contig)
   return contigs

contigs = ContigGeneration(G)
print Covert(contigs)
    