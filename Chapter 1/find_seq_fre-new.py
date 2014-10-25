def find_clump(genome, k, L, t):
    
    result=[]
    while L<len(genome):
      i=0
      while i<L:
            a=genome[0:L].count(genome[i:i+k])
            #print a, genome[j:j+k], i, j
            if a>=t and genome[i:i+k] not in result:
                #num.append(a)
                result.append(genome[i:i+k])
            i+=1
        #print genome
      genome=genome[k:]
    print result, len(result)
f=open('E-coli.txt', 'r')
genome=f.read()
genome=genome.translate(None, '\n')
f.close()
find_clump(genome, 9, 500, 3)