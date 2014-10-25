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

with open("7_7.txt") as r1:
    text = (r1.readline()).translate(None, "\n")
    patterns = (r1.readline()).translate(None, "\n")
    patterns = patterns.split()
    d = int((r1.readline()).translate(None, "\n"))
    
print len(text), len(patterns), d
    #t = (r.readline()).translate(None, "\n")
#s = "ACATGCTACTTT" 
#patterns = ["ATT", "GCC", "GCTA", "TATT"]
#k = 1
#print s[233:]

def find_match(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
def find_pattern(s, pattern, k):
    dist = 0
    for j in range (0, len(pattern)):
        if s[j] != pattern[j]:
            dist += 1
        if dist > k:
                break
       # print dist        
    if dist <= k:
       return True
    else:
        return False

def split_into(n, d):
    l = n / d
    a = n % d
    s = 0
    for _ in range(d):
        e = s + l
        if a > 0:
            a -= 1
            e += 1
        yield s, e
        s = e

def find_all(text, pattern, d):
    pos = []
    seeds_index = list(split_into(len(pattern), d + 1))
    #print seeds_index
    for (i,j) in seeds_index:
        indexs = list(find_match(text, pattern[i:j]))
        for index in indexs:
            #print index, i
            if index - i > 0 and index -i + len(pattern) < len(text) + 1:
               if find_pattern(text[index - i: index - i + len(pattern)], pattern, d):
                   if index - i not in pos:
                       pos += [index - i]
    return pos        
positions = []
for pattern in patterns:
   positions += find_all(text, pattern, d)
print sorted(positions)
 