import math
import os
import random
import re
import sys



n = int(input())
if n>1 and n<1000000:
    x= bin(n)
    num = x.rsplit("0") 
    joe =0
    for i in num :
        count = i.count("1")  
        if count >= joe:
             joe = count

    print (joe)
