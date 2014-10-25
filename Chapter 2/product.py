import itertools

from mass import mass_of_AA
#from product import gen_list
#from masssubp import masssubpeptides
temp = mass_of_AA ()
mass_AA = []
for AA in temp:
    mass_AA.append(temp[AA])
mass_AA.pop()

f = open('7_5.txt', 'r')
Spectrum1 = f.read()
f.close
#print Spectrum1
Spectrum1 = Spectrum1.translate(None, '\n')
Spectrum1 = Spectrum1.split()
Spectrum = []
for num in Spectrum1:
    Spectrum.append(int(num))    
#print Spectrum[-1], type(Spectrum[0])
#Spectrum = [0,113,128,186,241,299,314,427]    
#Spectrum = [0,71,113,115,129,131,137,147,156,163,186,227,244,244,250,257,262,284,292,317,319,381,388,390,391,397,399,407,413,430,448,501,512,519,528,528,544,554,563,567,576,634,638,641,643,657,691,705,707,710,714,772,781,785,794,804,820,820,829,836,847,900,918,935,941,949,951,957,958,960,967,1029,1031,1056,1064,1086,1091,1098,1104,1104,1121,1162,1185,1192,1201,1211,1217,1219,1233,1235,1277,1348]
seed = {}
Spectrum.sort()
length = 0
mass = []
for element in Spectrum:
    for AA in temp:
      if element == temp[AA]:
        seed[AA] = element
        length+=1

def gen_list(seed, num):
    new_list = [' '.join(item) for item in itertools.product([seed1 for seed1 in seed], repeat=num)]
    return new_list
print gen_list(seed, length), len(gen_list(seed, length))