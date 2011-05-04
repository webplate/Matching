#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testsuite import *
import time

joker = u"~"

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

#le plus simple
def learner(sample):
    #sélectionne le premier mot (dans l'ordre canonique)
    w=min_can(sample)
    l=len(w)
    p=list(joker*l)
    for i in range(l):
        p[i]=w[i] #essaye de spécialiser le motif
        for word in sample:
            if not match(word,p) :
                p[i]=joker #revient sur essai si sur-spécialisé
                break
    return "".join(p)

def match_sample(sample,p):
    for word in sample:
        if not match(word,p):
            return False
    return True

def patt(s):
    if s != None:
        return "~"+"~".join(s)+"~"
    else:
        return "~"

def ok(s,cand,sample):
    c=s[:].append(cand)
    return match_sample(sample,patt(c))

def learner2(sample):
    w=list(min_can(sample))
    l=len(w)
    s=[]
    i = 0
    while i < l:
       cand=""
       j = i
       while ok(s,cand,sample) and j < l:
           cand += w[j]
           j += 1
       if cand != "":
           s.append(cand)
       i += len(cand) + 1
    return patt(s)


def main():
    t=time.time()
    #~ print min_can2(["c","ab","aa","c","g"])
    print match(t0, pp)
    inference=learner(temp)
    lag=time.time() - t
    logfile=open("learner.log","ab")
    message="New :\n"+inference+"\n"+str(lag)+"\n"

    logfile.write(message.encode('utf-8'))
    logfile.close()
    print lag
    return 0

if __name__ == '__main__':
    main()
