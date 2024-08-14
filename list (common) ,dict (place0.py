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



def have_common_member(list1, list2):
    """Check if two lists have at least one common member."""
    for item in list1:
        if item in list2:
            return True
    return False

# Example data sets
list_a1 = [1, 2, 3, 4, 5]
list_a2 = [5, 6, 7, 8, 9]

list_b1 = ['apple', 'banana', 'cherry']
list_b2 = ['grape', 'melon', 'banana']

list_c1 = ['car', 'bike', 'bus']
list_c2 = ['plane', 'boat', 'train']

# Call the function with different data sets
result1 = have_common_member(list_a1, list_a2)
result2 = have_common_member(list_b1, list_b2)
result3 = have_common_member(list_c1, list_c2)

# Print the results
print(f"Do list_a1 and list_a2 have at least one common member? {result1}")
print(f"Do list_b1 and list_b2 have at least one common member? {result2}")
print(f"Do list_c1 and list_c2 have at least one common member? {result3}")






























