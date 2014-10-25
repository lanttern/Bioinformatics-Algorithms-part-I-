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

with open("7_6.txt") as r1:
    s = (r1.readline()).translate(None, "\n")
    patterns = []
    for line in r1:
       patterns.append(line.translate(None, "\n"))
    
#print s, patterns
    #t = (r.readline()).translate(None, "\n")
#s = "AATCGGGTTCAATCGGGGT" 
#patterns = ["ATCG", "GGGT"]
#print s[233:]
l = len(s)
Index = []
def is_dpattern (pattern):
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[0]:
            return i
            break
def find_pattern(s, pattern):
    global Index
    i = is_dpattern (pattern)
    while len(s) >= len(pattern):
        if pattern in s:
           a = s.find(pattern) + l - len(s)
           if a not in Index:
              Index.append(a)
        else:
            break
        s = s[i:]
        
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
Positions = [find_pattern(s, pattern) for pattern in patterns]
print sorted(Positions[-1])
