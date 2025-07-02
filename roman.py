class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'),
            (500, 'D'),
            (100, 'C'),
            (50, 'L'),
            (10, 'X'),
            (5, 'V'),
            (1, 'I')
        ]

    def convert(self, num):
        roman = ''
        for value, symbol in self.value_map:
            while num >= value:
                roman += symbol
                num -= value
        return roman

converter = IntegerToRoman()

number = 1987
print(f"Integer: {number}")
print("Roman Numeral:", converter.convert(number))
