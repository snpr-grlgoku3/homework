class StringReverser:
    def __init__(self, text):
        self.__text = text  

    def reverse_words(self):
        words = self.__text.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

    def __str__(self):
        return f"Original: {self.__text}\nReversed: {self.reverse_words()}"

input_text = "Encapsulation makes code clean"
reverser = StringReverser(input_text)
print(reverser)
