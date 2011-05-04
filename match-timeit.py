#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testsuite import *
import timeit

joker = "~"
#p = "A~Lorem~D"

w=word
p=short_pattern

def createGraphe(p):
        graphe=[]
        q=0
        for c in p:
                graphe.append((q,q+1,c))
                if c==joker:
                        graphe.append((q+1,q+1,c))
                q+=1
        return graphe

#print createGraphe(p)

def match(w,p):
        q=[True]
        for i in range(len(p)):
                q.append(False)
        graphe=createGraphe(p)
        for c in w:
                s=q[:]
                for j in range(len(q)):
                        if q[j]:
                                if (j,j+1,c) in graphe:
                                        s[j+1]=True
                                if (j,j,joker) not in graphe:
                                        s[j]=False
                                if (j,j+1,joker) in graphe:
                                        s[j+1]=True
                q=s
        return q[-1]



def match2(w,p):
    q=[True]
    n=len(p)
    for i in range(n):
        q.append(False)

    for c in w:
        s=q[:]
        for j in range(n+1):
            s[j] = (q[j-1] and (p[j-1] == c or p[j-1] == joker))\
            or (q[j] and p[j-1] == joker)
        q=s
    return q[-1]


#print match(w,p)
#print match2(w,p)

if __name__=="__main__":
    from timeit import Timer
    #~ t1 = Timer("match(w,p)", "from __main__ import *")
    #~ t2 = Timer("match2(w,p)", "from __main__ import match2,w,p")
    print match2(t0,pp)
    #~ print t1.timeit(5)
    #~ print t2.timeit(5)/5
