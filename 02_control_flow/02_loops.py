"""
Topic: 02_loops
Source: freeCodeCamp Python

This file demonstrates loops (for and while) for repeating code blocks
and iterating over sequences.
"""

# ============================================================================
# FOR LOOP WITH RANGE()
# ============================================================================

print("=== FOR LOOP WITH RANGE() ===\n")

# Basic range: range(stop)
print("for i in range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

# range with start and stop: range(start, stop)
print("for i in range(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print("\n")

# range with step: range(start, stop, step)
print("for i in range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

# Negative step (counting down)
print("for i in range(5, 0, -1):")
for i in range(5, 0, -1):
    print(i, end=" ")
print("\n\n")


# ============================================================================
# FOR LOOP WITH LISTS
# ============================================================================

print("=== FOR LOOP WITH LISTS ===\n")

fruits = ["apple", "banana", "cherry", "date"]

print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Using enumerate to get index and value
print("\nWith indices:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")
print()


# ============================================================================
# FOR LOOP WITH STRINGS
# ============================================================================

print("=== FOR LOOP WITH STRINGS ===\n")

word = "Hello"

print(f"Characters in '{word}':")
for char in word:
    print(f"  {char}")
print()


# ============================================================================
# NESTED FOR LOOPS
# ============================================================================

print("=== NESTED FOR LOOPS ===\n")

# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()
print()


# ============================================================================
# WHILE LOOP
# ============================================================================

print("=== WHILE LOOP ===\n")

# Basic while loop
print("Count from 1 to 5:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print("\n")

# While loop with condition
print("While loop with condition:")
num = 10
while num > 0:
    print(num, end=" ")
    num -= 2
print("\n\n")


# ============================================================================
# PRACTICE EXAMPLE 1: PRINTING A PATTERN
# ============================================================================

print("=== PRACTICE 1: TRIANGLE PATTERN ===\n")

for i in range(1, 6):
    print("*" * i)
print()


# ============================================================================
# PRACTICE EXAMPLE 2: SUM OF NUMBERS
# ============================================================================

print("=== PRACTICE 2: SUM OF NUMBERS ===\n")

total = 0
for i in range(1, 11):
    total += i

print(f"Sum of 1 to 10: {total}")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: MULTIPLICATION TABLE
# ============================================================================

print("=== PRACTICE 3: MULTIPLICATION TABLE ===\n")

number = 7

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i:2d} = {result:2d}")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: COUNTING DOWN
# ============================================================================

print("=== PRACTICE 4: COUNTDOWN ===\n")

print("Launching in:")
for i in range(10, 0, -1):
    print(i, end="... " if i > 1 else "...\n")
print("Blastoff! 🚀\n")


# ============================================================================
# PRACTICE EXAMPLE 5: AVERAGE SCORE
# ============================================================================

print("=== PRACTICE 5: AVERAGE SCORE ===\n")

scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)

print(f"Scores: {scores}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: FINDING MAXIMUM
# ============================================================================

print("=== PRACTICE 6: FIND MAXIMUM ===\n")

numbers = [34, 12, 56, 23, 78, 45, 89]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")
print()


# ============================================================================
# PRACTICE EXAMPLE 7: FILTERING EVEN NUMBERS
# ============================================================================

print("=== PRACTICE 7: EVEN NUMBERS ONLY ===\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Original: {numbers}")
print(f"Even numbers: {even_numbers}")
print()


# ============================================================================
# PRACTICE EXAMPLE 8: FACTORIAL CALCULATION
# ============================================================================

print("=== PRACTICE 8: FACTORIAL ===\n")

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is {factorial}")
print()


# ============================================================================
# PRACTICE EXAMPLE 9: CHARACTER FREQUENCY
# ============================================================================

print("=== PRACTICE 9: CHARACTER FREQUENCY ===\n")

text = "hello world"
char_count = {}

for char in text:
    if char != " ":  # Skip spaces
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print(f"Text: '{text}'")
print("Character frequencies:")
for char, count in char_count.items():
    print(f"  '{char}': {count}")
print()


# ============================================================================
# PRACTICE EXAMPLE 10: NUMBER GUESSING GAME
# ============================================================================

print("=== PRACTICE 10: GUESSING GAME (SIMULATED) ===\n")

# Simulated game (without actual user input to keep output clean)
secret_number = 42
attempts = 0
guesses = [30, 50, 45, 40, 42]  # Simulated guesses

print(f"Secret number: {secret_number}")
print("Guessing process:")

for guess in guesses:
    attempts += 1
    if guess == secret_number:
        print(f"  Attempt {attempts}: Guessed {guess} - Correct! 🎉")
        break
    elif guess < secret_number:
        print(f"  Attempt {attempts}: Guessed {guess} - Too low")
    else:
        print(f"  Attempt {attempts}: Guessed {guess} - Too high")

print(f"Game completed in {attempts} attempts!")
print()


# ============================================================================
# WHILE LOOP WITH USER SIMULATION
# ============================================================================

print("=== PRACTICE 11: WHILE LOOP PATTERN ===\n")

# Simulated user input
count = 0
max_iterations = 5

print("While loop running 5 times:")
while count < max_iterations:
    count += 1
    print(f"  Iteration {count}")
print()


# ============================================================================
# NESTED LOOPS - GRID PATTERN
# ============================================================================

print("=== PRACTICE 12: GRID PATTERN ===\n")

print("3x3 Grid:")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()
print()


# ============================================================================
# PRACTICE EXAMPLE 13: DIAMOND PATTERN
# ============================================================================

print("=== PRACTICE 13: DIAMOND PATTERN ===\n")

size = 5

# Upper half
for i in range(size):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))

# Lower half
for i in range(size - 2, -1, -1):
    print(" " * (size - i - 1) + "*" * (2 * i + 1))
print()


# ============================================================================
# PRACTICE EXAMPLE 14: WORD REVERSAL
# ============================================================================

print("=== PRACTICE 14: REVERSE WORDS ===\n")

words = ["hello", "world", "python"]

print("Original words:")
for word in words:
    print(f"  {word}")

print("\nReversed words:")
for word in words:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(f"  {reversed_word}")
print()


# ============================================================================
# PRACTICE EXAMPLE 15: FIZZBUZZ
# ============================================================================

print("=== PRACTICE 15: FIZZBUZZ ===\n")

print("FizzBuzz (1-20):")
for i in range(1, 21):
    output = ""
    
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    
    if not output:
        output = str(i)
    
    print(output, end=" ")
print("\n\n")


# ============================================================================
# QUICK CHALLENGES
# ============================================================================

print("=== CHALLENGES ===")
print("1) Print the alphabet (a-z) using a loop.")
print("2) Calculate the sum of squares from 1 to 10.")
print("3) Create a 5x5 multiplication table.")
print("4) Count how many times a character appears in a string.")
print("5) Find all prime numbers from 1 to 50.")
print("6) Create a pattern of increasing and decreasing stars.")
print("7) Reverse a list without using the reverse() method.")
print("\nTry implementing these!\n")

print("=== END OF LOOPS EXAMPLES ===")
