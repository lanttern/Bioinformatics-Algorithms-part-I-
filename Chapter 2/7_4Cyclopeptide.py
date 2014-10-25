# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:04:11 2013
Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).

CODE CHALLENGE: Solve the Generating Theoretical Spectrum Problem.

Sample Input:
     LEQN

Sample Output:
     0 113 114 128 129 227 242 242 257 355 356 370 371 484
"""
from mass import mass_of_AA
temp = mass_of_AA ()
mass_AA = []
for AA in temp:
    mass_AA.append(temp[AA])
mass_AA.pop()
mass_AA = set(mass_AA)
mass = 1024
print mass_AA

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

def Mass_peptide(mass):
    if mass == 0:
        return 1
    if mass < 0:
        return 0
    else:
        return sum([Mass_peptide(mass-item) for item in mass_AA])
print Mass_peptide(mass)
