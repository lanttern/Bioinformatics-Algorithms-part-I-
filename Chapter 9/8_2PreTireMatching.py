# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie
CODE CHALLENGE: Implement TRIEMATCHING to solve the Multiple Pattern Matching Problem.
     Input: A string Text and a collection of strings Patterns.
     Output: All starting positions in Text where a string from Patterns appears as a substring.

Sample Input:
     AATCGGGTTCAATCGGGGT
     ATCG
     GGGT

Sample Output:
     1 4 11 15
"""
patterns = []
with open("8_2.txt") as r:
    text = (r.readline()).translate(None, "\n")
    for line in r:
        patterns.append(line.translate(None, "\n"))

#text = "AATCGGGTTCAATCGGGGT"
#patterns = ["ATCG", "GGGT"]

l = sum([len(i) for i in patterns])

#l = len(pattern)
def TirePattern (patterns, l):
    tires = [dict() for x in range(l + 2)]
    end = 2
    #print tires
    for pattern in patterns:
       start = 1 
       for s in pattern:
         if s in tires[start]:
             start = tires[start][s]
         else:
             #print start, end, s
             tires[start][s] = end
             start = end
             end += 1
             #print start, end, s
             #start = end
        

    return tires

def PreTireMatch(Text, Tire):
    #print Text
    symbol = Text[0]
    start = 1
    i = 1
    while True:
        if symbol in Tire[start]:
            start = Tire[start][symbol]
            symbol = Text[i]
            i += 1
            if i >= len (Text):
                return True
                break
        elif Tire[start] == {}:
            #print Text[:i-1]
            return True
        else:
            #print "no matches found"
            return False
def TireMatching (text, Tire):
    j = 0
    while len(text) >= min([len(i) for i in patterns]):
        #print text
        d = PreTireMatch(text, Tire)
        #print d
        if d:
            print j
        j += 1
        text = text[1:]
        #print text

Tire = TirePattern (patterns, l)       
print Tire
TireMatching (text, Tire)   
            
