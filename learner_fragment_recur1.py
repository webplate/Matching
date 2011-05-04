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

def patt(s):
    if s != None:
        return "~"+"~".join(s)+"~"
    else:
        return "~"

def match_sample(sample,p):
    for word in sample:
        if not match(word,p):
            return False
    return True

def learner(sample):
    w = min_can(sample)
    p = build_patt(sample, w)
    return patt(p)

def build_patt(sample, w, p=[], position=0):
    #condition d'arrêt
    if w == "":
        return []
    l = len(w)
    #recherche fragment le plus gros qui matche
    found = False
    for k in range (l, 0, -1) :
        for i in range(0,l-k+1) :
            cand = w[i:i+k]
            p.insert(position, cand)
            #~ print p, match_sample(sample, p)
            if match_sample(sample, p):
                found = True
            else :
                p.pop(position)
            if found : break
        if found : break
    if found :
        #rappel la fonction sur les parties restantes du mot
        ante = w[:i]
        post = w[i+k:]
        #~ print "ante", ante, "post", post, "patt", p
        p_ante = build_patt(sample, ante, p, position)
        p_post = build_patt(sample, post, p, position+1)
        p = p_ante + [cand] + p_post
        return p
    else :
        return []

def main():
    t=time.time()
    #~ print match("abcabccba", ["a", "bc"])
    inference=learner(short_sample2)
    lag=time.time() - t
    logfile=open("learner.log","ab")
    message="New :\n"+inference+"\n"+str(lag)+"\n"
    logfile.write(message.encode('utf-8'))
    logfile.close()
    print lag
    return 0

if __name__ == '__main__':
    main()
