def add_car_record(cars, car_id):
    print(f"Enter details for Car {car_id}:")
    color = input("Color: ")
    model = input("Model: ")
    brand = "Toyota"  # As the company must be Toyota
    transmission = input("Transmission (Automatic/Manual): ")
    cars[car_id] = {"Color": color, "Model": model, "Brand": brand, "Transmission": transmission}

def print_car_record(cars, car_id):
    if car_id in cars:
        print(f"Car {car_id} Record: {cars[car_id]}")
    else:
        print(f"Car {car_id} does not exist.")

def update_car_record(cars, car_id):
    if car_id in cars:
        print(f"Updating Car {car_id} Record:")
        color = input("New Color: ")
        model = input("New Model: ")
        brand = "Toyota"  # As the company must be Toyota
        transmission = input("New Transmission (Automatic/Manual): ")
        cars[car_id] = {"Color": color, "Model": model, "Brand": brand, "Transmission": transmission}
        print(f"Updated Car {car_id} Record: {cars[car_id]}")
    else:
        print(f"Car {car_id} does not exist.")

def main():
    cars = {}

    # a) Add the record of THREE cars separately by taking inputs at runtime whose company must be Toyota and display it.
    for i in range(1, 4):
        add_car_record(cars, i)

    # Print all car records
    for car_id in cars:
        print_car_record(cars, car_id)

    # b) Print the record of second car present and update it with new information and display.
    print("\nRecord of second car:")
    print_car_record(cars, 2)
    update_car_record(cars, 2)

    # c) Add new car record in the dictionary and print each car record individually.
    print("\nAdding a new car record:")
    add_car_record(cars, 4)
    for car_id in cars:
        print_car_record(cars, car_id)

    # d) Remove the third car record from the dictionary and display the remaining cars
    print("\nRemoving the third car record:")
    if 3 in cars:
        del cars[3]
    for car_id in cars:
        print_car_record(cars, car_id)

if __name__ == "__main__":
    main()
