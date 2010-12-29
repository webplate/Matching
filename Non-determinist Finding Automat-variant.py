#!/usr/bin/env python
# -*- coding: utf-8 -*-

joker="~"

def delta_from_pattern(pattern, alphabet):
    state=0
    relations=[]
    for c in pattern:
        if c == joker:
            for char in alphabet:
                relations.append((state, char, state))
        else:
            relations.append((state, c, state+1))
            state+=1
    delta=[]
    state+=1
    for i in range(state):
        delta.append([])
        for j in range(state):
            delta[i].append([])
            for c in alphabet:
                if (i, c, j) in relations:
                    delta[i][j].append(True)
                else:
                    delta[i][j].append(False)
    return delta,state

def match(pattern, word):
    #genere alphabet
    alphabet=""
    for c in pattern:
        if c not in alphabet and c != joker:
            alphabet+=c
    for c in word:
        if c not in alphabet and c != joker:
            alphabet+=c
    #genere delta
    delta, states = delta_from_pattern(pattern, alphabet)
    #initialise les vecteurs de position
    curr=[]
    next=[]
    for i in range(states):
        curr.append(False)
        next.append(False)
    #active état init
    curr[0]=True
    for c in word:
        if True in curr:
            print "#########",c
            for i in range(states):
                if curr[i]:
                    for j in range(states):
                        e = alphabet.index(c)
                        #si prochain état accessible
                        if delta[i][j][e]:
                            next[j] = True
                        #ou s'il est transitoire
                        elif i == j:
                            next[j] = False
            curr=next[:]
            print curr
    #si l'état final est atteint
    return curr[-1]

print match("a~a~k~", "aasgklzhkg")
