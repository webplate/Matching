#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testsuite import *


joker = "~"

def createGraphe(p):
	graphe=[]
	q=0
	for c in p:
		graphe.append((q,q+1,c))
		if c==joker:
			graphe.append((q+1,q+1,c))
		q+=1
	return graphe

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

print match(t1,"~<~")
