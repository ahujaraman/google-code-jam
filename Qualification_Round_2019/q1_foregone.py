# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:18:51 2019

@author: raman
"""

def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)


def split_two(T):
    n = int(input())
    digits = []
    p1 = []
    val = n
    
    while n:
        digit = n%10
        digits.insert(0,digit)
        n = n//10
    
    
    for i in range(len(digits)):
        if digits[i] == 4:
            p1.append(1)
        else:
            p1.append(digits[i])
    part1 = magic(p1)
    part2 = val - part1
    print("Case #{}: {} {}".format(T,part1,part2))
    return



T = int(input())
for i in range(1,T+1):
    split_two(i)