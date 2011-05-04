#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testsuite import *
import time

joker = u"~"

def match(w,p):
    current=0
    wlen=len(w)
    i=0
    #pour chaque fragments
    for f in p:
        #~ print f
        l=len(f)
        #on le cherche dans le mot
        while i+l < wlen+1:
            #~ print i,l,w[i:i+l],w[i:i+l] == f
            if w[i:i+l] == f:
                current += 1
                i += l
                break
            i += 1
    return current == len(p)

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

def learner(sample):
    w=list(min_can(sample))
    l=len(w)
    p=list(joker*l)
    for i in range(l):
        p[i]=w[i]
        for word in sample:
            matching=match(word,p)
            #print "".join(p), matching, word
            if not matching:
                p[i]=joker
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
    if cand != u"":
        p = s + [cand]
    else:
        return True
    print "#match?#", p, match(sample[1], p)
    print match_sample(sample,p)
    return match_sample(sample,p)

def learner2(sample):
    w=min_can(sample)
    l=len(w)
    s=[]
    i = 0
    while i < l:
        cand=u""
        j = i
        print "newcand",cand,"on letter", w[j]
        while ok(s,cand,sample) and j < l:
            print "cand",cand
            cand += w[j]
            j += 1
        #retire dernière lettre ajoutée
        #sauf si on est à la fin du mot
        if j != l :
            cand = cand[:-1]
        if cand != "":
            print "append", cand
            s.append(cand)
            i += len(cand)
        i += 1
    return patt(s)

def main():
    t=time.time()
    #~ print match(t4, [u'<title>', u'l'])
    inference=learner2(temp)
    lag=time.time() - t
    logfile=open("learner.log","ab")
    message="New :\n"+str(inference)+"\n"+str(lag)+"\n"
    logfile.write(message.encode('utf-8'))
    logfile.close()
    print lag
    return 0

if __name__ == '__main__':
    main()














