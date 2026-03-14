def greet():
    print("Hello")
    print("Welcome!")
    print("Goodbye!")

def greet_with_name(name):
    print(f"Hello, {name}!")
    print("Welcome!")


def greet(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

greet(name="Jack", location="Virginia")
