# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie

k = 3
s = "AAACTCATC"
t = "TTTCAAATCCAAATAAA"

"""
with open("4_4.txt") as r:
    k = int((r.readline()).translate(None, "\n"))
    s = (r.readline()).translate(None, "\n")
    t = (r.readline()).translate(None, "\n")
nt = {"A":"T", "T":"A", "C":"G", "G":"C"}
def shared (k, s, t):
    a = []
    for j in range(0, len(s)-k + 1):
        n = t.count(s[j:k+j])
        m = t.count(RS(s[j:k+j]))
        #print RS(s[j:k+j])
        if n > 0:
            i = t.index(s[j:k+j])
            if (j, i) not in a:
               print (j, i)
               a.append((j, i))
        while 1 < n:
            i = find_next(i, t[i+1:], s[j:k+j])
            if (j, i) not in a:
               print (j, i)
               a.append((j, i))
            n -= 1
        if m > 0:
            l = t.index(RS(s[j:k+j]))
            if (j, l) not in a:
               print (j, l)
               a.append((j, l))
        while m > 1:
            l = find_next(l, t[l+1:], RS(s[j:k+j]))
            if (j, l) not in a:
               print (j, l)
               a.append((j, l))
            m -= 1
    print len(a) 
def find_next(ind, s1, s2):
    return ind + 1 + s1.index(s2)
    
def RS(string):
    RCstring = ''
    i = len(string) - 1
    while i >= 0:
        RCstring += nt[string[i]]
        i -= 1
    return RCstring    

shared (k, s, t)