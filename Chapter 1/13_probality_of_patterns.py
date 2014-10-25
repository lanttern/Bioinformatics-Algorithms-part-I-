from product import gen_list
array=gen_list('01',4)
print array
Sum=0.0
for item in array:
    if '01' not in item:
      Sum+=1
print Sum
print 1.0-Sum/(2**4)