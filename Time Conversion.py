#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s2=s[-2:]
    s3=s[2:-2]
    s4=int(s[:2])
    if s2=="AM":
        if s4==12:
            s5="00"+s3
        else:
            s5=s[:-2]
        return s5
    elif s2=="PM":
        if s4==12:
            s5="12"+s3
        else:
            s4+=12
            s5=str(s4)+s3
    return s5
        
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
   
    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
