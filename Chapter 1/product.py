import itertools
def gen_list(seed, num):
    new_list = [''.join(item) for item in itertools.product(seed, repeat=num)]
    return new_list
print gen_list('01', 4)
c = gen_list('01', 4)
d = c[0]
for i in range(1, len(c)):
    d += c[i][-1]
print d