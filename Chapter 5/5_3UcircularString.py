# -*- coding: utf-8 -*-
"""
CODE CHALLENGE: Solve the k-Universal Circular String Problem.
     Input: An integer k.
     Output: A k-universal circular string.

Sample Input:
     4

Sample Output:
     0000110010111101
@author: zhihuixie
"""
with open('5_3.txt') as r:
    n = int((r.readline()).translate(None, '\n'))
n = 4
k = 4
print n

def de_bruijn(k, n):
    """
    De Bruijn sequence for alphabet size k 
    and subsequences of length n.
    """
    a = [0] * k * n
    #print a
    sequence = []
    def db(t, p):
        if t > n:
           # print t, p
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return sequence
  
path = de_bruijn(k, n)
print path
           #if len(path) == G.size():
    #print path
cycle = ''
for edge in path:
    cycle += str(edge)
print cycle
