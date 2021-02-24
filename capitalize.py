#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    str_list = s.split(" ")
    result = ""
    for word in str_list:
        result += word.capitalize() + " "
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['/home/adminp/ankit/hackerrank_py/text_file.txt'], 'w')
    fptr = open('/home/adminp/ankit/hackerrank_py/text_file.txt', 'w')

    s = input()

    result = solve(s)
    print(">>>: ", result)
    fptr.write(result + '\n')

    fptr.close()
