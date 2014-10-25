def Skew(genome):
    n=0
    result=[0]
    for i in genome:
        if i=='G':
           n+=1
        if i=='C':
           n-=1
        result.append(n)
    print result

genome='GAGCCACCGCGATA'
Skew(genome)