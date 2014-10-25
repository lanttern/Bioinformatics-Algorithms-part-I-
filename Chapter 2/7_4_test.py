# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:06:35 2013
this code no matter order of AA string
@author: zhihuixie
"""
from mass import mass_of_AA
temp = mass_of_AA ()
mass_AA = []
for AA in temp:
    mass_AA.append(temp[AA])
mass_AA.pop()
mass = 128
mass_AA.sort()
print mass_AA
target = mass
coins = mass_AA
ways = [1]+[0]*target
print ways[0]
for coin in coins:
    for i in range(coin-1, target+1):
        #print i
        ways[i]+=ways[i-coin]
print sum(ways)
print ways[target]