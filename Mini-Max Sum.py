#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minSum,maxSum=0,0
    for i in range(5):
        minSum+=arr[i]
        maxSum+=arr[i]
        if i==0:
            maxSum-=arr[i]
        elif i==4:
            minSum-=arr[i]
    print(minSum,maxSum)
            

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
