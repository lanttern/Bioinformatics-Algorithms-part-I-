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

with open("7_7test.txt") as r1:
    s = (r1.readline()).translate(None, "\n")
    patterns = (r1.readline()).translate(None, "\n")
    patterns = patterns.split()
    k = int((r1.readline()).translate(None, "\n"))
    
print len(s), len(patterns), k
    #t = (r.readline()).translate(None, "\n")
#s = "ACATGCTACTTT" 
#patterns = ["ATT", "GCC", "GCTA", "TATT"]
#k = 1
#print s[233:]
Index  = []
def find_pattern(s, pattern, k):
    global Index
    n = len(pattern)
    m = len(s)
    for i in range(0, m - n + 1):
        dist = 0
        for j in range (0, n):
            if s[i + j] != pattern[j]:
                dist += 1
            if dist > k:
                break
       # print dist        
        if dist <= k:
            Index.append(i)
    return Index
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
find_pattern = Memoize(find_pattern)   
positions = [find_pattern(s, pattern, k) for pattern in patterns]
print sorted(positions[-1])