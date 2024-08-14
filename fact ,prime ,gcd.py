
'''Write a program to print all prime numbers from 900 to 1000. [Hint: Use nested loops, break and continue]'''

# Loop through numbers from 900 to 1000
for num in range(900, 1001):
    # Assume the number is prime until proven otherwise
    is_prime = True
    # Check for factors from 2 to the number before num
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # Exit the loop if a factor is found
    # Print the number if it is prime
    if is_prime and num > 1:
        print(num)


'''factorial and twicw of it'''


# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Initialize variables
total_sum = 0

# Calculate the sum of the series for the first seven terms
for i in range(1, 8):
    term = i / factorial(i)
    total_sum += term

# Add twice the sum of the series to itself
final_result = total_sum + 2 * total_sum

# Print the final result
print("Result:", final_result)


'''gcd'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input numbers
num1 = 24
num2 = 36

# Calculate and print GCD
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)










