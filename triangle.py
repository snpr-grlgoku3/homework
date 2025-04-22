n = int(input("Enter the number of rows: "))

# Top half (normal right-angled triangle)
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * i
    print(spaces + stars)

# Bottom half (inverted right-angled triangle)
for i in range(n - 1, 0, -1):
    spaces = ' ' * (n - i)
    stars = '*' * i
    print(spaces + stars)