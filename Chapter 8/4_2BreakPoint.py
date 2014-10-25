# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie

"""
p = []
with open("4_2.txt") as r:
    s = (r.readline()).translate(None, '\n')
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.split()
    for el in s:
        p.append(int(el))
#print p
#p = [+3, +4, +5, -12, -8, -7, -6, +1, +2, +10, +9, -11, +13, +14]
#print len(p)
def BP(p):
    bp = 0
    if p[0] != 1:
        bp += 1
    if p[-1] != len(p):
        bp += 1
    for i in range (0, len(p)-1):
       if p[i+1] - p[i] != 1:
           if p[i+1] > 0 and p[i] > 0:
              bp += 1
           elif p[i+1] < 0 and p[i] < 0:
              if p[i+1] - p[i] != -1:
                 bp += 1
           else:
               bp += 1
    print bp
        
BP(p)