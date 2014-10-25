# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie

"""
import networkx as nx
p = []
count, countj = 0, 0
with open("4_3.txt") as r:
    s = (r.readline()).translate(None, '\n')
    s = s.replace("(", "")
    s = s.replace(")", " A ")
    s = s.split()
    t = (r.readline()).translate(None, '\n')
    t = t.replace("(", "")
    t = t.replace(")", " B ")
    t = t.split()
    #print s, t
    for i in range (1, len(s) + 1):
        #print p, count, i
        if i == len(s):
            break
        if s[i] == "A":
            #print (int(s[i-1]), -int(s[i-count-1]))
            p.append((int(s[i-1]), -int(s[i-count-1])))
            count = 0
        else:
            if s[i-1] != "A":
          #  print s[i]
               p.append((int(s[i-1]), -int(s[i])))
               count += 1
    for j in range (1, len(t) + 1):
        #print p, count, i
        if j == len(t):
            break
        if t[j] == "B":
            #print (int(s[i-1]), -int(s[i-count-1]))
            p.append((int(t[j-1]), -int(t[j-countj-1])))
            countj = 0
        else:
            if t[j-1] != "B":
          #  print s[i]
               p.append((int(t[j-1]), -int(t[j])))
               countj += 1
#print p

G = nx.Graph(p)
#print len(G)
Cycles = len(nx.cycle_basis(G)) + (len(p) - len(G.edges()))
Blocks = len(G.nodes())/2
Distance = Blocks - Cycles
#print len(G.edges()), len(G.nodes())
#print len(nx.cycle_basis(G))
print Distance
#p = [+3, +4, +5, -12, -8, -7, -6, +1, +2, +10, +9, -11, +13, +14]
#print len(p)

"""
"""
def cycle_basis(G,root=None):
    """ Returns a list of cycles which form a basis for cycles of G.

    A basis for cycles of a network is a minimal collection of
    cycles such that any cycle in the network can be written
    as a sum of cycles in the basis.  Here summation of cycles
    is defined as "exclusive or" of the edges. Cycle bases are
    useful, e.g. when deriving equations for electric circuits
    using Kirchhoff's Laws.

    Parameters
    ----------
    G : NetworkX Graph
    root : node, optional
       Specify starting node for basis.

    Returns
    -------
    A list of cycle lists.  Each cycle list is a list of nodes
    which forms a cycle (loop) in G.

    Examples
    --------
    >>> G=nx.Graph()
    >>> G.add_cycle([0,1,2,3])
    >>> G.add_cycle([0,3,4,5])
    >>> print(nx.cycle_basis(G,0))
    [[3, 4, 5, 0], [1, 2, 3, 0]]

    Notes
    -----
    This is adapted from algorithm CACM 491 [1]_.

    References
    ----------
    .. [1] Paton, K. An algorithm for finding a fundamental set of
       cycles of a graph. Comm. ACM 12, 9 (Sept 1969), 514-518.

    See Also
    --------
    simple_cycles
    """
    gnodes=set(G.nodes())
    cycles=[]
    while gnodes:  # loop over connected components
        if root is None:
            root=gnodes.pop()
        stack=[root]
        pred={root:root}
        used={root:set()}
        while stack:  # walk the spanning tree finding cycles
            z=stack.pop()  # use last-in so cycles easier to find
            zused=used[z]
            for nbr in G[z]:
                if nbr not in used:   # new node
                    pred[nbr]=z
                    stack.append(nbr)
                    used[nbr]=set([z])
                elif nbr == z:        # self loops
                    cycles.append([z])
                elif nbr not in zused:# found a cycle
                    pn=used[nbr]
                    cycle=[nbr,z]
                    p=pred[z]
                    while p not in pn:
                        cycle.append(p)
                        p=pred[p]
                    cycle.append(p)
                    cycles.append(cycle)
                    used[nbr].add(z)
        gnodes-=set(pred)
        root=None
    return cycles
