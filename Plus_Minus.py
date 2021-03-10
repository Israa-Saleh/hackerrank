#!/bin/python3

import math
import os
import random
import re
import sys
def positive(arr):
    d=0
    for i in arr:
        if i>0:
            d+=1
    return d
def Negative(arr):
    d=0
    for i in arr:
        if i<0:
            d+=1
    return d
def Zero(arr):
    d=0
    for i in arr:
        if i==0:
            d+=1
    return d
# Complete the plusMinus function below.
def plusMinus(arr):
    d1=positive(arr)/len(arr)
    print("{:.6f}".format(d1))
    d2=Negative(arr)/len(arr)
    print("{:.6f}".format(d2))
    d3=Zero(arr)/len(arr)
    print("{:.6f}".format(d3))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
