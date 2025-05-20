test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Test Dictionary:")
print(test_dict)

key_to_check = input("Enter the key to check its frequency: ")

if key_to_check in test_dict:
    print(f"Frequency of '{key_to_check}':", test_dict[key_to_check])
else:
    print(f"'{key_to_check}' not found in the dictionary.")