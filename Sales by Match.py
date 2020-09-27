#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    #creating an empty dictionary
    shoes=[]
    pairs =0
    for i in ar:
        if i not in shoes:
            shoes.append(i)
            cnt= ar.count(i)
            pairs+= cnt//2
    return pairs
if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print (result)
