def register():
    print("\n___ Welcome to the Health and Wellness App ___\n")
    name = input("Please enter your name-------------------: ")
    age = int(input("Please enter your age--------------------: "))
    weight = float(input("Please enter your weight in kg-----------: "))
    height = float(input("Please enter your height in meters-------: "))
    calories = int(input("Please enter your daily calorie goal-----: "))
    water = int(input("Please enter your daily water goal in ml-: "))

    with open("user_data.txt", "w") as file:
        file.write(f"Enter Your Name-----------: {name}\n")
        file.write(f"Enter Your Age------------: {age}\n")
        file.write(f"Enter Your Weight---------: {weight}\n")
        file.write(f"Enter Your Height---------: {height}\n")
        file.write(f"Enter Your Calories Goal--: {calories}\n")
        file.write(f"Enter Your Water Goal-----: {water}\n")
    print("User registered successfully!\n")


def food_Intake():
    enter_food_item = input("\nEnter the food name---------------: ")
    calories = int(input("Enter the calories consumed-------: "))
    with open("food_Intake.txt", "a") as file:
        file.write(f"{enter_food_item} - {calories} calories\n")
    print("Food Intake logged successfully!\n")


def water_Intake():
    enter_water_item = int(input("\nEnter the amount of water consumed in ml: "))
    with open("water_Intake.txt", "a") as file:
        file.write(f"{enter_water_item} ml\n")
    print("Water intake logged successfully!\n")


def show_display():
    try:
        with open("user_data.txt", "r") as file:
            user_data = file.read()
            print("\n---- Register User ----")
            print(user_data)

        with open("food_Intake.txt", "r") as file:
            food = file.read()
            if food:
                print("\n--- Food Intake ---")
                print(food)
            else:
                print("\nFood is empty...")

        with open("water_Intake.txt", "r") as file:
            water = file.read()
            if water:
                print("\n--- Water Intake ---")
                print(water)
            else:
                print("\nWater is empty...")
    except FileNotFoundError:
        print("User data not found...")


def run():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == "yes" and password == "ok":
        print()
        print("\n             Login successful!              ")
        print("\n=== Welcome to Health and Wellness App ===\n")

    while True:
        print()
        print("1. Register User!")
        print("2. Food Intake!")
        print("3. Water Intake!")
        print("4. Show Display!")
        print("5. Exit.")
        choose = input("Choose your option: ")
        if choose  == '1':
            register()
        elif choose  == '2':
            food_Intake()
        elif choose  == '3':
            water_Intake()
        elif choose  == '4':
            show_display()
        elif choose  == '5':
            print("Thank you for using this App!")
            break
        else:
            print("Invalid choice...")

if __name__ == "__main__":
    run()


