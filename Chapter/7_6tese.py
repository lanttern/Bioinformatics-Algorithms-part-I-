s = "ATCATC"
def Cycle (s):
    array = [s]
    l = len(s)
   # print l
    i = 1
    while i < l:
       temp = s[l-i:] + s[:l-i] 
       array.append(temp)
       i += 1
    return sorted(array)
Last = ''.join(a[-1] for a in Cycle (s))

First = "".join(sorted(Last))
print First, Last, Cycle (s)
C = {"A":0, "C":Last.count("A"), "G":Last.count("C") + Last.count("A"), "T":Last.count("G") + Last.count("C") + Last.count("A")}


def Occ (c, k):
    return Last[:k+1].count(c)
def LtoF(c, k):
    return C[c] + Occ (c,k) - 1
def BWMatch(pattern):
    top = 0
    bottom = len(Last) - 1
    while top <= bottom:
        #print len(pattern)
        if len(pattern) != 0:
            symbol = pattern[-1]   
            if symbol in Last[top:bottom + 1]:
                R ="".join([Last[i] for i in range(bottom, top - 1, -1)])
                topIndex = Last[top:bottom + 1].index(symbol) + top
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
            
positions = BWMatch("TAA")
print positions