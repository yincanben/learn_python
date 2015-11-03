#!/usr/bin/env python
# coding=utf-8
import random,string
chars = string.letters+string.digits

class Activation_Code(object):
    def create_random_string(self,num,length=6):
        f=open("./activation_code.txt","w")
        #chars = string.letters + string.digits
        for _ in range(num):
            print Activation_Code.concatenate(self,4)
            #random_str=[random.choice(chars) for i in range(length)]
            f.write(Activation_Code.concatenate(self,4)+'\n')
        f.close()
    def getRandom(self):
        global chars
        return "".join(random.sample(chars,6))
    def concatenate(self,group):
        return "-".join([Activation_Code.getRandom(self) for i in range(group)])

if __name__ =='__main__':
    obj = Activation_Code()
    obj.create_random_string(200,6)
