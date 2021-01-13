"""It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state. If anyone has bribed more than two people, the line is too chaotic to compute the answer.

Function Description:

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):

int q[n]: the positions of the people after all bribes


Returns

No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
"""




import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    sorted_list = sorted(q)
    lis = [sorted_list.index(i)- q.index(i) for i in sorted_list if sorted_list.index(i)>q.index(i)]
    qis = [abs(q.index(i) - sorted_list.index(i))  for i in sorted_list ]
    if max(lis) >2:
        print("Too chaotic")
    else:
        print(sum(set(qis)))
    print(lis, qis)

if __name__ == '__main__':
    n = int(input('Enter number of inputs: '))
    list =[]
    for i in range(n):
        list.append(input('Enter a number: '))

    minimumBribes(list)
