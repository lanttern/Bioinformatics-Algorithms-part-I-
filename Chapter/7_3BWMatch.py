# -*- coding: utf-8 -*-
"""
 BWMATCHING(FirstColumn, LastColumn, Pattern, LastToFirst)
        top ← 0
        bottom ← |LastColumn| − 1
        while top ≤ bottom
            if Pattern is nonempty
                symbol ← last letter in Pattern
                remove last letter from Pattern
                if positions from top to bottom in LastColumn contain an occurrence of symbol
                    topIndex ← first position where symbol occurs among positions where symbol occurs from 
                                        top to bottom in LastColumn
                    bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
                    top ← LastToFirst(topIndex)
                    bottom ← LastToFirst(bottomIndex)
                else
                    output 0
            else
                output bottom − top + 1

"""
#from suffix_tree1 import SuffixTree, print_node

with open("7_3.txt") as r1:
    r = (r1.readline()).translate(None, "\n")
    patterns = (r1.readline()).translate(None, "\n")
    patterns = patterns.split()
    
#print r, patterns
    #t = (r.readline()).translate(None, "\n")
#r = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC" 
#patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
s = "".join(sorted(r))
C = {"$":0, "A":1, "C":r.count("A") + 1, "G":r.count("C") + r.count("A") + 1, "T":r.count("G") + r.count("C") + r.count("A") + 1}


def Occ (c, k):
    return r[:k+1].count(c)
def LtoF(c, k):
    return C[c] + Occ (c,k) - 1
def BWMatch(pattern):
    top = 0
    bottom = len(r) - 1
    while top <= bottom:
        #print len(pattern)
        if len(pattern) != 0:
            symbol = pattern[-1]
            
            if symbol in r[top:bottom + 1]:
                R ="".join([r[i] for i in range(bottom, top - 1, -1)])
                topIndex = r[top:bottom + 1].index(symbol) + top
                bottomIndex = len(R) - 1 - R.index(symbol) + top
                #print topIndex, bottomIndex
                top = LtoF(symbol, topIndex)
                bottom = LtoF(symbol, bottomIndex)
                #print top, bottom
            else:
                return 0
                break
        else:
            #print bottom, top
            return bottom - top + 1
            break
        pattern = pattern[:-1]
            
positions = [BWMatch(pattern) for pattern in patterns]
print positions
