#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testsuite import *
import time

joker = u"~"

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

def match0(w,p):
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

def match(w,p):
    q=[True]
    n=len(p)
    for i in range(n):
        q.append(False)

    for c in w:
        s=q[:]
        for j in range(1,n+1):
            #~ print s
            #~ s[j] = (q[j] and p[j-1] == joker) or (q[j-1] and (p[j-1] == joker or p[j-1] == c))
            s[j] =  (q[j-1] and (p[j-1] == c or p[j-1] == joker)) or (q[j] and p[j-1] == joker)
        s[0] = False
        q=s
    return q[-1]

def min_can(list):
    #~ pourquoi s'interesser à l'ordre lexicographique????
    #~ list.sort()
    #on selectionne le plus court
    min=float('+inf')
    select=0
    for i in range(len(list)):
        l=len(list[i])
        if l < min:
            min=l
            select=i
    return list[select]

#~ def min_can2(list):
    #~ min=float('+inf')
    #~ for w in list:
        #~ l=len(w)
        #~ if l < min:
            #~ min=l
    #~ shortest=[]
    #~ for w in list:
        #~ if len(w) == min:
            #~ shortest.append(w)
    #~ if len(shortest) != 1:
        #~ shortest.sort()
    #~ return shortest[0]
#plus simple
def learner(sample):
    w=min_can(sample)
    l=len(w)
    p=list(joker*l)
    for i in range(l):
        p[i]=w[i]
        for word in sample:
            matching=match(word,p)
            print "".join(p), matching, word
            if not matching:
                p[i]=joker
                break
    return "".join(p)

def learner2(sample):
    w=min_can(sample)
    l=len(w)
    p=[]
    for i in range(l):
        p.append(w[i])
        p.append(joker)
        for word in sample:
            matching=match(word,p)
            print "".join(p), "\n", matching, "\n", word
            if not matching:
                p=p[:-2]
                p.append(joker)
                break
        if matching:
            p=p[:-1]
    return "".join(p)

def main():
    t=time.time()
    #~ print min_can2(["c","ab","aa","c","g"])
    print match(t1, p0)
    inference=learner2(temp)
    lag=time.time() - t
    logfile=open("learner.log","ab")
    message="New :\n"+inference+"\n"+str(lag)+"\n"

    logfile.write(message.encode('utf-8'))
    logfile.close()
    print lag
    return 0

if __name__ == '__main__':
    main()
