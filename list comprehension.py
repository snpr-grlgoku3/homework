num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
odd_numbers_alt = [i for i in range(1, num + 1, 2)]
print("Odd numbers under input:", odd_numbers)


fruits = ['apple', 'banana', 'cherry', 'mango']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("fruit list:", capitalized_fruits)
