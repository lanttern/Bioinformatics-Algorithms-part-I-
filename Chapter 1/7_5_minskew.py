def Skew_min(genome):
    n=0
    result=[0]
    j=0
    for i in genome:
        if i=='G':
           n+=1
        if i=='C':
           n-=1
        result.append(n)
    print min(result)
    while j<len(result):
        if result[j]==min(result):
           print j
        j+=1
f=open('7_5_minskew.txt', 'r')
genome=f.read()
genome=genome.translate(None,'\n')
Skew_min(genome)