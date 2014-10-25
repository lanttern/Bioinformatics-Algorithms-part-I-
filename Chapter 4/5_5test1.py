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
import copy
graph = []
with open ('5_5.txt') as r:
    for line in r:
        line = line.translate(None, '\n')
        line = line.replace(' -> ', ' ')
        line = line.replace(',', ' ')
        line = line.split()
        temp = []
        for i in range (1, len(line)):
            graph.append((int(line[0]),int(line[i])))
l = len(graph)
#print graph
def find_tour(u,E, tour):  
  for (a,b) in E:
    if a==u:
        tour.append(b)
        E.remove((a,b))
        find_tour(b,E,tour)
   # elif b==u:
    #    E.remove((a,b))
     #   find_tour(a,E,tour)
  return tour

def EulerianCycle(G):
    for i in range (0,l):
           g = copy.deepcopy(G)
           tour = [g[i][0], g[i][1]]
           g.remove(tuple(tour))
           cycle = find_tour(tour[-1],g,tour)
           if len(cycle) >= l:
              return cycle
           print 'progress is: ' + str((i+1)*1.0*100/l) + '%'
    #return cycle + [cycle[0]]

path = EulerianCycle(graph)
cycle1 = ''
for node in path:
   cycle1 += str(node)+'->'
print cycle1[:-2]