# Program to determine a person's stage of life based on age

# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Determine the stage of life based on the age
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
    
'''invitation'''

# Initial list of guests
guests = ["Alice", "Bob", "Charlie", "David"]

# Printing initial invitations
print("Initial invitations:")
for guest in guests:
    print(f"Dear {guest}, please join us for dinner!")

# Assume Charlie can't make it, so replace him with Emily
cancelled_guest = "Charlie"
new_guest = "Emily"

# Find the index of the cancelled guest
index_to_replace = guests.index(cancelled_guest)

# Insert the new guest at the found index
guests.insert(index_to_replace, new_guest)

# Print new invitations
print("\nNew invitations:")
for guest in guests:
    print(f"Dear {guest}, please join us for dinner!")












