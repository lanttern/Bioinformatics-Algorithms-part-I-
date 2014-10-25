# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
Spectral Convolution Problem: Compute the convolution of a spectrum.
     Input: A collection of integers Spectrum.
     Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should
     appearexactly k times; you may return the elements in any order.

CODE CHALLENGE: Solve the Spectral Convolution Problem.

Sample Input:
     0 137 186 323

Sample Output:
     137 137 186 186 323 49
"""
from mass import mass_of_AA
#import itertools
#from product import gen_list
#from masssubp import masssubpeptides
temp = mass_of_AA ()
mass_AA = []
for AA in temp:
    mass_AA.append(temp[AA])
mass_AA.pop()
'''
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize
'''

f = open('7_6test.txt', 'r')
Spectrum1 = f.read()
f.close
#print Spectrum1
Spectrum1 = Spectrum1.translate(None, '\n')
Spectrum1 = Spectrum1.split()
Spectrum = []
for num in Spectrum1:
    Spectrum.append(int(num)) 
Spectrum.sort()    

#print Spectrum[-1], type(Spectrum[0])
#Spectrum = [0, 137, 186, 323]    
#Spectrum = [0,71,113,115,129,131,137,147,156,163,186,227,244,244,250,257,262,284,292,317,319,381,388,390,391,397,399,407,413,430,448,501,512,519,528,528,544,554,563,567,576,634,638,641,643,657,691,705,707,710,714,772,781,785,794,804,820,820,829,836,847,900,918,935,941,949,951,957,958,960,967,1029,1031,1056,1064,1086,1091,1098,1104,1104,1121,1162,1185,1192,1201,1211,1217,1219,1233,1235,1277,1348]

def Spectral_Convolution (Spectrum):
    list1=[]
    final_list = []
    for i in range(0, len(Spectrum)):
        for j in range (0, len(Spectrum)-1):
            if Spectrum[i] > Spectrum[j]:
                list1.append(Spectrum[i]-Spectrum[j])
                count1 = list1.count(Spectrum[i]-Spectrum[j])
                if count1 >=1:
                   final_list.append(Spectrum[i]-Spectrum[j])
    final_list.sort()
    return final_list
print Spectral_Convolution (Spectrum)

            
                