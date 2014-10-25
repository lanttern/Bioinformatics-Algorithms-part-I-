# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie
CODE CHALLENGE: Solve the Trie Construction Problem.
     Input: A collection of strings Patterns.
     Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has
     n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in
     any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first
     two members of the triple must be the integers labeling the initial and terminal nodes of the edge,
     respectively; the third member of the triple must be the symbol labeling the edge.

Sample Input:
     GGTA
     CG
     GGC

Sample Output:
     1 2 G
     2 3 G
     3 4 T
     4 5 A
     3 6 C
     1 7 C
     7 8 G
"""

with open("8_3test.txt") as r:
    s = (r.readline()).translate(None, "\n")

#s = "AAAAAAAAAATATCGTTTTATCAAAAAAAAAGTT"
def LongestRepeats(string):
    l = len(string)
    max_length = 1
    print l
#print substring
    i = 0
    substring = []
    while i < l:
        j = 0
        while j <= i:
            if string[j:l-i + j] not in substring:
                substring.append(string[j:l-i + j])
                if string.count(string[j:l-i + j]) > 1:
                    if len(string[j:l-i + j]) > max_length:
                        max_length = len(string[j:l-i + j])
                        longest_repeats = string[j:l-i + j]
            j += 1
        i += 1
        print i
    #print max_length, longest_repeats
    return longest_repeats

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
LongestRepeats = Memoize(LongestRepeats)     
print LongestRepeats(s)