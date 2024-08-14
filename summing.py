# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:54:01 2024

@author: hiraa
"""

num = int(input("Enter any number: "))
sum = 0

for x in range (1,num+1):
    sum+=x             #this is correct
    # sum = num+ x    #this is wronggggg
print(sum)

# list = [22,444,666,569509,88]

# sum = 0
# for x in list:
#     sum += x
#     print(sum)