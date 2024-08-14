# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:37:39 2024

@author: hiraa
"""

# list1 = [ ]*10

# for x in range(10):
    
#     list1[x] = int(input("enter 10 no to add in list1: "))
    
# print(list1)



########correct

# list1 = []

# for x in range(1,11  ):
    
#     i= int(input("enter 10 no to add in list1: "))
#     list1+= [i]
# print(list1)

# check=int(input("enter to check no in list: "))

# if check in list1:
#     print("yes it is present")


# else:
#         print("no its is not")


###############user input and store if even
list1 = []

for x in range(1,11  ):
    
    i= int(input("enter 10 no to add in list1: "))
    if i%2==0:
        list1+= [i]

print(list1)


























# list1 = [0] * 10

# # Loop to take 10 integers as input
# for x in range(10):
#     list1[x] = int(input("Enter a number to add to list1: "))

# # Print the list of integers
# print("The list of integers is:", list1)

    