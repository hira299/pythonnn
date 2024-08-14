# a = [23,45,67,876,33,45,645,657]  ###().list not possibke
# print(type(a))

# import random
# random.shuffle(a)
# print(a)

# dict1 = {1:[3,5,6,7,8,0]}

# for k,v in dict1.items():
#     for no in v:
#         print(k,no)
# a=[]

# for x in range(6):
#     i = int(input("enter no :"))
#     a+=[i]
# print(a)

# a=[]

# for x in range(6):
#     i = int(input("enter no :"))
#     a.append(i)
# print(a)



# Dictionary of favorite places
favorite_places = {
    "Alice": ["Bear Mountain", "Death Valley", "Tierra Del Fuego"],
    "Bob": ["Grand Canyon", "Yellowstone", "Yosemite"],
    "Charlie": ["Paris", "Tokyo", "New York"]
}

# Loop through the dictionary and print each person’s name and their favorite places
for person,places in favorite_places.items():
    print(f"{person} likes the following places:")
    for place in places:
       print(f"{place}")

































