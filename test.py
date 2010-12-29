#!/usr/bin/env python
# -*- coding: utf-8 -*-

def match(w,p):
    #TODO generate delta from p
    #delta from exo=[[1,4], [2,0], [4,3], [4,1], [4,4]]

    #p="0~1"
    #delta=[[1,4], [2,2], [2,3], [2,3], [4,4]]
    #final=[3]
    #p="0~0"
    #delta=[[1,4], [2,2], [3,2], [3,2], [4,4]]

    #p="0~1~0"
    delta=[[1,6], [2,2], [2,3], [4,4], [5,3], [5,3], [6,6]]
    final=[5]
    init=0
    #explore states according to word
    q=init
    for i in range(len(w)):
        wi=int(w[i])
        q=delta[q][wi]
    return q in final

print match("000011110","p")
