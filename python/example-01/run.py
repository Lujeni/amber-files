import math
import os

from typing import List, Dict, Any

def list_operations():
    """Perform operations on a list of fruits."""
    fruits: list[str] = ["apple", "banana", "cherry"]
    fruits.append("date")
    print(f"Fruits: {fruits}")

def greeting(name: str) -> str:
    """Return a greeting message.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message.
    """
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"

def dictionary_operations():
    student: dict[str, any] = {"name": "John", "age": 21, "courses": ["Math"]}
    student["grade"] = "A"
    print(f"Student: {student}")

def set_operations():
    colors: set[str] = {"red", "green", "blue"}
    colors.add("yellow")
    print(f"Colors: {colors}")

def tuple_operations():
    coordinates: tuple[float, float] = (10.0, 20.0)
    print(f"Coordinates: {coordinates}")

def add(a: int, b: int) -> int:
    return a + b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

operations: dict[str, callable] = {
    "add": add,
    "divide": divide
}

def test_functions_and_lambdas():
    print("=== Functions and Lambdas ===")
    for name, func in operations.items():
        print(f"{name}: {func(10, 5)}")

    def square(x):
        return x * x
    print(f"Square of 5: {square(5)}")

class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self) -> str:
        return f"{self.name} barks"

def test_classes_and_objects():
    print("=== Classes and Objects ===")
    animal = Animal("Generic Animal", "Unknown")
    dog = Dog("Buddy", "Golden Retriever")

    print(animal.make_sound())
    print(dog.make_sound())

def math_operations():
    print(f"Pi: {math.pi}")
    print(f"Square root of 16: {math.sqrt(16)}")

def os_operations():
    print(f"Current directory: {os.getcwd()}")
    print(f"List directory: {os.listdir('.')}")

def test_modules_and_imports():
    print("=== Modules and Imports ===")
    math_operations()
    os_operations()

# File I/O
def write_to_file(filename: str, content: str):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()

def test_file_io():
    print("=== File I/O ===")
    filename = "test.txt"
    content = "Hello, World!\nThis is a test file."
    write_to_file(filename, content)
    print(f"Content of {filename}:")
    print(read_from_file(filename))

# Exception Handling
def divide_with_exception_handling(a: int, b: int) -> str:
    try:
        return str(a / b)
    except ZeroDivisionError as e:
        return f"Error: {e}"

def test_exception_handling():
    print("=== Exception Handling ===")
    print(divide_with_exception_handling(10, 2))
    print(divide_with_exception_handling(10, 0))

def typing_example(numbers: List[int], text: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {
        "count": len(numbers),
        "text_length": len(text),
        "squares": [x ** 2 for x in numbers]
    }
    return result

def test_typing():
    print("=== Typing Example ===")
    numbers = [1, 2, 3, 4, 5]
    text = "Hello"
    result = typing_example(numbers, text)
    print(f"Typing Example Result: {result}")
