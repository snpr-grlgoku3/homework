# Define the Dog class
class Dog:
    # Class variable
    species = "DOGS"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    # Method to display dog details
    def display_details(self):
        print(f"Species: {Dog.species}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years\n")

dog1 = Dog("Golden Retriever", 5)
dog2 = Dog("German Shepherd", 3)
dog3=Dog("Poodle",5)

dog1.display_details()
dog2.display_details()
dog3.display_details()
