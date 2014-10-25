f=open('E-coli.txt', 'r')
seq=f.read()
seq=seq.translate(None, '\n')
i=0
num=[]
k=5
result=[]
while i<=len(seq)-k:
    a=seq.count(seq[i:i+k])
    if a>1:
       num.append(a)
    #print num
    i+=1
print num
#print new_list[num.index(max(num))]
for j in range(len(num)):
    #print j
    if num[j]==max(num) and seq[j:j+k] not in result:
        result.append(seq[j:j+k])
print result