
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    sorted_list = sorted(q)
    lis = [sorted_list.index(i)- q.index(i) for i in sorted_list if sorted_list.index(i)>q.index(i)]
    if max(lis) >2:
        print("Too Chaotic")
    else:
        print (sum(lis))

if __name__ == '__main__':
    n = int(input('Enter number of inputs: '))
    list =[]
    for i in range(n):
        list.append(input('Enter a number: '))

    minimumBribes(list)
