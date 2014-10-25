# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:55:29 2013
CODE CHALLENGE: Solve the Eulerian Cycle Problem.
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.

Sample Input:
     0 -> 3
     1 -> 0
     2 -> 1,6
     3 -> 2
     4 -> 2
     5 -> 4
     6 -> 5,8
     7 -> 9
     8 -> 7
     9 -> 6

Sample Output:
     6->8->7->9->6->5->4->2->1->0->3->2->6
@author: zhihuixie
"""
graph = {}
with open ('5_5test.txt') as r:
    for line in r:
        line = line.translate(None, '\n')
        line = line.replace(' -> ', ' ')
        line = line.replace(',', ' ')
        line = line.split()
        temp = []
        for i in range (1, len(line)):
            temp.append(int(line[i]))
            graph[int(line[0])] = temp
#print graph
import copy
from random import choice
def EulerianCycle(G):  
    unexposed = copy.deepcopy(G)
    starts = [node for node in G if len(G[node]) == 1]
    stack = [unexposed[item] for item in unexposed]
    total = len(stack)
    exposed = [choice(starts)]
    #exposed = [1140]
    exposed.append(unexposed[exposed[0]][0])
    del unexposed[exposed[0]][0]
    while stack:
        v = exposed[-1]
       # print 'start'
       # print exposed, unexposed
        if unexposed[v] == []: 
            #v = exposed[-1]
            g = copy.deepcopy(G)
            if v == exposed[0]:# wrong cycle
                exposed.pop()
            else:               #not a cycle
               exposed.pop() # del node
               c = []
               for i in range(0, len(exposed)):
                   if exposed[i] == v:
                       c.append(exposed[i+1])
               b = [el for el in g[v] if el not in c]
               #b.append(g[a][-1])
               unexposed[v] = b      # add node back as unexposed
            a = exposed[-1]
            if unexposed[a] != []: # add node back
               d = unexposed[a]
               d.append(v)
               unexposed[a] = d
        else:
            #g1 = copy.deepcopy(G)
            u = unexposed[v][0]
            exposed.append(u)
            #print unexposed[v][0]
            #n = unexposed[v][0]
            del unexposed[v][0]  
        stack = [unexposed[item] for item in unexposed if unexposed[item] != []]
        print exposed     
        print 'Progress is: ' + str((1.0 - 1.0*len(stack)/total)*100) + '%'
        #print unexposed            
    return exposed
 
        
#graph ={0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[5,8],7:[9],8:[7],9:[6]}    
path = EulerianCycle(graph)
cycle1 = ''
for node in path:
   cycle1 += str(node)+'->'
print cycle1[:-2]
