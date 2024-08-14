

# def greet(name):
#     print(f"Hello, {name}!")

# user_name = input("Enter your name: ")
# greet(user_name)


# def multiply_numbers(a, b):
#       return a * b

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = multiply_numbers(num1, num2)
# print(f"Multiplication result: {result}")

# import calendar
# yy= 2024
# mm= 6
# print(calendar.month(yy,mm))



shopping_list =[]


def add_item(item):
     if item != 'quit':
        shopping_list.append(item)

def print_list_items(list1):
     print("this is your list")
     for items in list1:
         print(items)

while True:
     item = input("add item. when finish write quit: ").lower()
     if item != 'quit':
      print(f"{item} added to shopping list.")
      add_item(item)
    
     else:
         print("list is finish")
         break

print_list_items(shopping_list)

























