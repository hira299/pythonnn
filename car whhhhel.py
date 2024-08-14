# def add_car_record(cars, car_id):
#     print(f"Enter details for Car {car_id}:")
#     color = input("Color: ")
#     model = input("Model: ")
#     brand = "Toyota"  # As the company must be Toyota
#     transmission = input("Transmission (Automatic/Manual): ")
#     cars[car_id] = {"Color": color, "Model": model, "Brand": brand, "Transmission": transmission}

# def print_car_record(cars, car_id):
#     if car_id in cars:
#         print(f"\nCar {car_id} Record: {cars[car_id]}")
#     else:
#         print(f"Car {car_id} does not exist.")

# def update_car_record(cars, car_id):
#     if car_id in cars:
#         print(f"Updating Car {car_id} Record:")
#         color = input("New Color: ")
#         model = input("New Model: ")  
#         brand = "Toyota"  # As the company must be Toyota
#         transmission = input("New Transmission (Automatic/Manual): ")
#         cars[car_id] = {"Color": color, "Model": model, "Brand": brand, "Transmission": transmission}
#         print(f"Updated Car {car_id} Record: {cars[car_id]}")
#     else:
#         print(f"Car {car_id} does not exist.")

# def main():
#     cars = {}

#     # a) Add the record of THREE cars separately by taking inputs at runtime whose company must be Toyota and display it.
#     for i in range(1, 4):
#         add_car_record(cars, i)

#     # Print all car records
#     print("\nAll Car Records:")
#     for car_id in cars:
#         print_car_record(cars, car_id)

#     # b) Print the record of second car present and update it with new information and display.
#     print("\nRecord of second car:")
#     print_car_record(cars, 2)
#     update_car_record(cars, 2)

#     # c) Add new car record in the dictionary and print each car record individually.
#     print("\nAdding a new car record:")
#     add_car_record(cars, 4)
#     for car_id in cars:
#         print_car_record(cars, car_id)

#     # d) Remove the third car record from the dictionary and display the remaining cars
#     print("\nRemoving the third car record:")
#     if 3 in cars:
#         del cars[3]
#     print("\nRemaining Car Records:")
#     for car_id in cars:
#         print_car_record(cars, car_id)


# main()
    
    
    
    
    
    
    
# list1=[]
# for i in range (3,9):
#     user=int(input("number:"))
#     x=user/3
#     list1.append(x)
# user1=int(input("enter a number to print value from the list:"))


# try:    
#     print(list1[user1])
# except:    
#     if user1 != len(list1):
#             raise Exception ('error nh aya')   
    
    
import math

def calculate_area_of_circle():
    
        radius = (input("Enter the radius of the circle: "))
    
        if type(radius) == str:
            raise Exception("input int")
            
        if radius <= 0:
      
            raise ValueError("Radius must be greater than zero.")
            
      
            
            
        area = math.pi * (radius ** 2)
        print(f"The area of the circle is: {area:.2f}")
 
calculate_area_of_circle()
    
    
    
    
# def operation(arr):
#     if len(arr) == 0:
#         return None, None
    
#     max_value = arr[0]
#     min_value = arr[0]
    
#     for num in arr:
#         if num > max_value:
#             max_value = num
#         if num < min_value:
#             min_value = num
    
#     return max_value, min_value

# # Example usage:
# array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# max_val, min_val = operation(array)

# if max_val is not None and min_val is not None:
#     print(f"The maximum value in the array is: {max_val}")
#     print(f"The minimum value in the array is: {min_val}")
# else:
#     print("The array is empty.")

    
   
    
# def calculate_simple_interest(amount, years, rate):
#     if rate < 1 or rate > 700:
#         raise Exception("Interest rate must be between 1 and 700.")
    
#     interest = (amount * years * rate) / 100
#     return interest

# # Example usage:
# amount = float(input("Enter the principal amount: "))
# years = float(input("Enter the number of years: "))
# rate = float(input("Enter the interest rate: "))

# calculate_simple_interest(amount, years, rate)
    
    
    

#   # List of appliance prices according to their index number
# prices = [0] * 11  # Initialize a list with 11 elements

# # Assign prices to the corresponding index
# prices[10] = 58000  # Washing machine
# prices[2] = 53500   # Dishwasher
# prices[5] = 60000   # Refrigerator
# prices[7] = 41700   # Television
# prices[4] = 10000   # Microwave oven
# prices[9] = 4500    # Kettle
# prices[3] = 95000   # Laptop
# prices[8] = 15400   # Iron
# prices[1] = 69000   # AC
# prices[6] = 30000   # Smartphone


# #in case of easiness

# for i in range(11):
#     a = input('fffffffffff : ')
    
#     prices[i]= a
    
# print(prices)
    
 

# # Remove the unused 0th index to have proper ordering


# # Step 3: Print the list of prices in separate lines
# print("Prices of appliances in ascending order of index:")
# for price in prices:
#     print(price)

# # Step 4: Remove the price of the laptop (index 3) and add the price of the printer (18000)
# prices[3] = 18000  # Index 3 in original list is 2 after removing the 0th element

# # Step 5: Print the updated list of prices in separate lines
# print("\nUpdated prices of appliances (replaced Laptop with Printer):")
# for price in prices:
#     print(price)

# # Step 6: Find the appliances with the highest price, lowest price, and neither expensive nor cheap
# max_price = max(prices)
# min_price = min(prices)

# # Print the results
# print(f"\nThe highest price is: {max_price}")
# print(f"The lowest price is: {min_price}")

# # Appliances neither most expensive nor least expensive
# print("Prices that are neither the highest nor the lowest:")
# for price in prices:
#     if price != max_price and price != min_price:
#         print(price)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
