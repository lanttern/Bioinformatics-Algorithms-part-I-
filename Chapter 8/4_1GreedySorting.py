# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:01:44 2014

@author: zhihuixie
GREEDYSORTING(P)
        approxReversalDistance ← 0
        for k = 1 to |P|
            if element k is not sorted
                apply the k-sorting reversal to P
                approxReversalDistance ← approxReversalDistance + 1
            if k-th element of P is −k
                apply the reversal flipping the k-th element of P
                approxReversalDistance ← approxReversalDistance + 1
        return approxReversalDistance
Sample Input:
     (-3 +4 +1 +5 -2)

Sample Output:
     (-1 -4 +3 +5 -2)
     (+1 -4 +3 +5 -2)
     (+1 +2 -5 -3 +4)
     (+1 +2 +3 +5 +4)
     (+1 +2 +3 -4 -5)
     (+1 +2 +3 +4 -5)
     (+1 +2 +3 +4 +5)

"""
p = []
with open("4_1.txt") as r:
    s = (r.readline()).translate(None, '\n')
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.split()
    for el in s:
        p.append(int(el))
#print p
#p = [-3, +4, +1, +5, -2, -9, 8, -7, 11, -10, 12, 6, 13, 14]
#print p
def GreedySorting(p):
    for k in range (1, len(p) + 1):
        q = p[:k-1]
        #print q, k-1
        if k in p:
            i = p.index(k)
        elif -k in p:
            i = p.index(-k)
                #print i, -k
        if k != p[k-1]: 
            for j in range (0, i+2-k):
                #print -p[i-j]
                q.append(-p[i-j])
            q +=  p[i+1:]
            print "(" + " ".join(["%+d" % i for i in q]) + ")"
        else:
            q += p[i:]
        if q[k-1] == -k:
            q[k-1] = k
            print "(" + " ".join(["%+d" % i for i in q]) + ")"
        p = q
GreedySorting(p)