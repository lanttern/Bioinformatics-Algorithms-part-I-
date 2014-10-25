def find_clump(genome, k, L, t):
    j=0
    #i,n=0,0
    #num=[]
    result,b=[],[]
    while j<=len(genome)-k:        
        if genome.count(genome[j:j+k])>=t and genome[j:j+k] not in b and len(b)<=4**k:
          b.append(genome[j:j+k])
        print j, len(b)
        j+=1
    #print b
    for item in b:
       print item
       i=0
       while i<=len(genome)-L:
            a=genome[i:L+i].count(item)
            #print item, a
              #print a, genome[j:j+k], i, j
            if a>=t and item not in result:
              #num.append(a)
                result.append(item)
            #print i
                i+=1
            #print i
#print n

    print len(result), result
f=open('E-coli.txt', 'r')
genome=f.read()
genome=genome.translate(None, '\n')
f.close()
find_clump(genome, 9, 500, 3)