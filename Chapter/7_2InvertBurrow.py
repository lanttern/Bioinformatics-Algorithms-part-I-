# -*- coding: utf-8 -*-
"""
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.
     Input: A string Text.
     Output: BWT(Text).

CODE CHALLENGE: Solve the Burrows-Wheeler Transform Construction Problem.

Sample Input:
     GCGTGCCTGGTCA$

Sample Output:
     ACTGGCT$TGCGGC

"""
#from suffix_tree1 import SuffixTree, print_node

with open("7_2.txt") as r:
    r = (r.readline()).translate(None, "\n")
    #t = (r.readline()).translate(None, "\n")
#r = "TTCCTAACG$A" 
"""
def ibwt(r):
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
       # print [r[i] + table[i] for i in range(len(r))]
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
       # print table
    #print table
    s = [row for row in table if row.endswith("$")][0]  # Find the correct row (ending in "\0")
    return s.rstrip("\0")  # Get rid of trailing null character
print ibwt(r)

"""
def ibwt(r, *args):
       # "Inverse Burrows-Wheeler transform. args is the original index \
       #  if it was not indicated by a null byte"
 
        firstCol = "".join(sorted(r))
        count = [0]*256
        byteStart = [-1]*256
        output = [""] * len(r)
        shortcut = [None]*len(r)
        #Generates shortcut lists
        for i in range(len(r)):
                shortcutIndex = ord(r[i])
                shortcut[i] = count[shortcutIndex]
                count[shortcutIndex] += 1
                shortcutIndex = ord(firstCol[i])
                if byteStart[shortcutIndex] == -1:
                        byteStart[shortcutIndex] = i
 
        localIndex = (r.index("$") if not args else args[0])
        for i in range(len(r)):
                #takes the next index indicated by the transformation vector
                nextByte = r[localIndex]
                output [len(r)-i-1] = nextByte
                shortcutIndex = ord(nextByte)
                #assigns localIndex to the next index in the transformation vector
                localIndex = byteStart[shortcutIndex] + shortcut[localIndex]
        return "".join(output).rstrip("\x00")
print ibwt(r)
print ibwt("enwvpeoseu$llt")