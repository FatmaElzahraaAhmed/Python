# 1. Accept user's first and last name, then print them in reverse order with a space between them.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Reversed name:", last_name, first_name)

# 2. Compute the value of n + nn + nnn (e.g., for n = 5, result is 5 + 55 + 555 = 615)
n = input("Enter an integer: ")
result = int(n) + int(n * 2) + int(n * 3)
print("Computed result of n + nn + nnn:", result)

# 3. Print a heredoc string (a multi-line string with specific formatting)
heredoc = """
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
print(heredoc)

# 4. Get the volume of a sphere with radius 6
import math
radius = 6
volume = (4/3) * math.pi * (radius ** 3)
print("Volume of a sphere with radius 6:", volume)

# 5. Compute the area of a triangle given its base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("Area of the triangle:", area)

# 6. Construct a pattern with nested for loops
# Print a pyramid-like pattern
n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()

# Reverse the pyramid pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 7. Accept a word from the user and reverse it
word = input("Enter a word to reverse: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# 8. Print all numbers from 0 to 6 except 3 and 6
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)

# 9. Get the Fibonacci series between 0 and 50
fibonacci = [0, 1]
while True:
    next_val = fibonacci[-1] + fibonacci[-2]
    if next_val > 50:
        break
    fibonacci.append(next_val)
fibonacci_output = " ".join(map(str, fibonacci[1:]))  # Skip the initial zero
print("Fibonacci series between 0 and 50:", fibonacci_output)

# 10. Accept a string and calculate the number of digits and letters
text = input("Enter a string: ")
digits = sum(c.isdigit() for c in text)
letters = sum(c.isalpha() for c in text)
print("Number of digits:", digits)
print("Number of letters:", letters)
