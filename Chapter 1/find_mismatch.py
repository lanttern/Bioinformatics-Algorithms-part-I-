def find_mismatch_pattern(pattern, genome, num_mismatch):
    l=len(pattern)
    m=len(genome)
    j=0
    result=[]
    seq=[]
    while l<len(genome):
      i=0
        #new_pattern=[]
      count=0
      while i<l:
          #new_pattern.append(genome[i])
          
          if pattern[i]==genome[i]:
              count+=1
          i+=1
    #print count
      if count>=l-num_mismatch:
          #new_pattern=''.join(new_pattern)
         result.append(j)
         seq.append(genome[0:l])
      j+=1
             #print j
      genome=genome[1:]
    print genome
    print result, seq
f=open('8_3_find_mismatch.txt', 'r')
pattern=f.readline()
pattern=pattern.translate(None,'\n')
genome=f.read()
genome=genome.translate(None, '\n')
#print pattern, genome
find_mismatch_pattern(pattern, genome,6)
