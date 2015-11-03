#!/usr/bin/env python
# coding=utf-8
import string,random
x=50
#global count 

#get the letters and digits
field = string.letters + string.digits

def getRandom(x):
    print x
    x =1 
    print x
    return "".join(random.sample(field,4))
def concatenate(group):
    global x
    return "-".join([getRandom(x) for i in range(group)])

def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__=='__main__':
    print generate(200)

