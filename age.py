age_input = input("Enter your age: ")
age = int(age_input)
if age < 0:
        raise ValueError("Age cannot be negative.")
if age % 2 == 0:
        print("The age entered is even.")
else:
        print("The age entered is odd.")

