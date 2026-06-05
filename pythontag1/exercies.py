# Python Exercises

## Lists

# 1. Create a list of five favorite fruits and print the third fruit.
# 2. Write a program that adds a new number to a list of numbers and then prints the updated list.
# 3. Given a list of names, write code to print the first and last item in the list.
# 4. Create a list of integers and print the length of the list using `len()`.
# 5. Write a program that replaces the second item in a list with a new value.

## If / Else

# 1. Ask the user for a number and print whether it is positive, negative, or zero.
# 2. Ask the user for their age and print `"You are an adult"` if the age is 18 or older; otherwise print `"You are a minor"`.
# 3. Write a program that checks if a number is even or odd and prints the result.
# 4. Ask the user for a password and print `"Access granted"` if the password is correct and `"Access denied"` otherwise.
# 5. Write a program that asks for a grade (0-100) and prints `"Pass"` if the grade is 50 or above, otherwise prints `"Fail"`.

## Functions

#1. Write a function called `greet()` that prints `"Hello, welcome!"` when called.

def greet():
    print("Hello, Welcome")
greet()

# 2. Create a function named `square(number)` that returns the square of the input and then call it with a sample value.


def square(number):
    return number **2
result=square(5)
print(result)

square(5)


# 3. Write a function `is_even(n)` that returns `True` if `n` is even and `False` if `n` is odd.

def is_even(n):
  if n % 2 == 0:
      return True
  else: return False

print(is_even(3))

# 4. Create a function `add_numbers(a, b)` that returns the sum of two numbers and print the result.

def add_numbers(a,b):
    return a + b
result= add_numbers(3,5)
print(result)


# 5. Write a function `favorite_food(food)` that prints `"My favorite food is {food}."` and call it with a sample food.

food= input("What is your favorite food? ")
def favorite_food(food):
    print(f"My favorite food is {food}.")
    
favorite_food(food)

## Combined Practice

# 1. Create a function that takes a list of numbers and returns the largest number. Test it with a sample list.
# 2. Write a program that asks the user for a list of three colors, then uses `if` / `else` to check if `"blue"` is in the list and prints a message.
# 3. Build a function that accepts a list and a value, then uses `if` / `else` to print whether the value is in the list or not.

