"""
Topic: 03_break_continue
Source: freeCodeCamp Python

This file demonstrates break and continue statements for controlling
loop flow and the else clause with loops.
"""

# ============================================================================
# BREAK STATEMENT
# ============================================================================

print("=== BREAK STATEMENT ===\n")

# break exits the loop immediately
print("for i in range(10) with break at 5:")
for i in range(10):
    if i == 5:
        print(f"  {i} - Breaking!")
        break
    print(f"  {i}")
print()


# ============================================================================
# BREAK WITH WHILE LOOP
# ============================================================================

print("=== BREAK WITH WHILE LOOP ===\n")

# Find first number divisible by 7
print("Finding first number divisible by 7:")
num = 1
while num <= 20:
    if num % 7 == 0:
        print(f"  Found: {num}")
        break
    print(f"  {num}")
    num += 1
print()


# ============================================================================
# CONTINUE STATEMENT
# ============================================================================

print("=== CONTINUE STATEMENT ===\n")

# continue skips current iteration and goes to next
print("for i in range(10) with continue at even numbers:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}")
print()


# ============================================================================
# CONTINUE WITH WHILE LOOP
# ============================================================================

print("=== CONTINUE WITH WHILE LOOP ===\n")

print("Skip numbers divisible by 3:")
num = 1
while num <= 10:
    num += 1
    if num % 3 == 0:
        continue  # Skip if divisible by 3
    print(f"  {num}")
print()


# ============================================================================
# ELSE WITH LOOPS
# ============================================================================

print("=== ELSE WITH LOOPS ===\n")

# else block runs if loop completes without break
print("Loop with else (no break):")
for i in range(3):
    print(f"  i = {i}")
else:
    print("  Loop completed without break!")
print()

# else block doesn't run if loop has break
print("Loop with else (with break):")
for i in range(5):
    if i == 2:
        print(f"  i = {i} - Breaking!")
        break
    print(f"  i = {i}")
else:
    print("  This doesn't print because of break")
print()


# ============================================================================
# PRACTICE EXAMPLE 1: SEARCH IN LIST
# ============================================================================

print("=== PRACTICE 1: SEARCH IN LIST ===\n")

items = ["apple", "banana", "cherry", "date", "elderberry"]
search_item = "cherry"

print(f"Looking for '{search_item}' in {items}")

found = False
for item in items:
    if item == search_item:
        print(f"Found '{search_item}'!")
        found = True
        break

if not found:
    print(f"'{search_item}' not found.")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: INPUT VALIDATION
# ============================================================================

print("=== PRACTICE 2: INPUT VALIDATION (SIMULATED) ===\n")

# Simulated input values
valid_inputs = ["yes", "no", "quit"]
test_inputs = ["maybe", "yes"]

print(f"Valid inputs: {valid_inputs}")

for user_input in test_inputs:
    if user_input not in valid_inputs:
        print(f"'{user_input}' is invalid. Try again.")
        continue
    
    print(f"'{user_input}' is valid!")
    
    if user_input == "quit":
        print("Exiting...")
        break
print()


# ============================================================================
# PRACTICE EXAMPLE 3: SKIP ODD NUMBERS
# ============================================================================

print("=== PRACTICE 3: SKIP ODD NUMBERS ===\n")

print("Numbers from 1 to 10 (skipping odd):")
for i in range(1, 11):
    if i % 2 == 1:  # Odd numbers
        continue
    print(f"  {i}")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: FIND FIRST PRIME
# ============================================================================

print("=== PRACTICE 4: FIND FIRST PRIME ===\n")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Finding first 5 prime numbers:")
count = 0
num = 2

while count < 5:
    if is_prime(num):
        print(f"  Prime #{count + 1}: {num}")
        count += 1
    num += 1
print()


# ============================================================================
# PRACTICE EXAMPLE 5: PROCESS UNTIL THRESHOLD
# ============================================================================

print("=== PRACTICE 5: PROCESS UNTIL THRESHOLD ===\n")

numbers = [10, 25, 30, 15, 50, 20, 60]
threshold = 45

print(f"Processing numbers until one exceeds {threshold}:")
for num in numbers:
    if num > threshold:
        print(f"  {num} - Exceeded threshold! Stopping.")
        break
    print(f"  {num} - OK")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: SKIP NEGATIVE NUMBERS
# ============================================================================

print("=== PRACTICE 6: SKIP NEGATIVE NUMBERS ===\n")

numbers = [5, -3, 10, -1, 7, -2, 4]

print(f"Processing: {numbers}")
print("Processing positive numbers only:")

for num in numbers:
    if num < 0:
        print(f"  {num} - Skipped (negative)")
        continue
    print(f"  {num} - Processed")
print()


# ============================================================================
# PRACTICE EXAMPLE 7: REMOVING DUPLICATES
# ============================================================================

print("=== PRACTICE 7: UNIQUE ITEMS ===\n")

items = ["apple", "banana", "apple", "cherry", "banana", "date"]
unique_items = []

print(f"Original: {items}")

for item in items:
    if item in unique_items:
        print(f"  {item} - Duplicate (skipped)")
        continue
    unique_items.append(item)
    print(f"  {item} - Added")

print(f"Unique items: {unique_items}")
print()


# ============================================================================
# PRACTICE EXAMPLE 8: STOP ON CONDITION
# ============================================================================

print("=== PRACTICE 8: STOP ON CONDITION ===\n")

print("Counting up, stopping when sum exceeds 30:")
total = 0
count = 0

while count < 10:
    count += 1
    total += count
    print(f"  Count: {count}, Total: {total}")
    
    if total > 30:
        print(f"  Sum exceeded 30! Stopping.")
        break
print()


# ============================================================================
# PRACTICE EXAMPLE 9: FILTER AND PROCESS
# ============================================================================

print("=== PRACTICE 9: FILTER AND PROCESS ===\n")

scores = [45, 92, 38, 85, 67, 91, 55]
passing_grade = 70

print(f"Scores: {scores}")
print(f"Passing grade: {passing_grade}")
print("Processing:")

for score in scores:
    if score < passing_grade:
        print(f"  {score} - Failing (skipped)")
        continue
    print(f"  {score} - Passing ✓")
print()


# ============================================================================
# PRACTICE EXAMPLE 10: SEARCH WITH RANGE
# ============================================================================

print("=== PRACTICE 10: SEARCH WITH RANGE ===\n")

target = 25

print(f"Searching for {target} from 1 to 50:")
for i in range(1, 51):
    if i == target:
        print(f"Found {target}!")
        break
    
    if i % 5 != 0:  # Skip non-multiples of 5
        continue
    
    print(f"  Checking {i}...")
print()


# ============================================================================
# PRACTICE EXAMPLE 11: NESTED LOOPS WITH BREAK
# ============================================================================

print("=== PRACTICE 11: NESTED LOOPS WITH BREAK ===\n")

print("Searching for target in 2D grid:")
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5

found = False
for row in grid:
    for num in row:
        print(f"  Checking {num}")
        if num == target:
            print(f"  Found {target}!")
            found = True
            break
    if found:
        break
print()


# ============================================================================
# PRACTICE EXAMPLE 12: MENU LOOP
# ============================================================================

print("=== PRACTICE 12: MENU LOOP (SIMULATED) ===\n")

print("Menu system (simulated):")
commands = ["help", "start", "quit"]

for cmd in commands:
    if cmd == "help":
        print(f"  Command: '{cmd}' - Showing help...")
        continue
    
    if cmd == "start":
        print(f"  Command: '{cmd}' - Starting...")
    
    if cmd == "quit":
        print(f"  Command: '{cmd}' - Exiting...")
        break
print()


# ============================================================================
# PRACTICE EXAMPLE 13: VALIDATION LOOP
# ============================================================================

print("=== PRACTICE 13: VALIDATION LOOP ===\n")

valid_ages = [18, 21, 25, 30, 35]
test_ages = [16, 25, 40]

print(f"Valid ages: {valid_ages}")
print("Testing ages:")

for age in test_ages:
    print(f"  Checking age {age}...")
    
    if age not in valid_ages:
        print(f"    Age {age} not in list (skipped)")
        continue
    
    print(f"    Age {age} is valid! ✓")
print()


# ============================================================================
# PRACTICE EXAMPLE 14: ELSE WITH SEARCH
# ============================================================================

print("=== PRACTICE 14: ELSE WITH SEARCH ===\n")

words = ["cat", "dog", "bird", "fish"]
search_word = "zebra"

print(f"Searching for '{search_word}' in {words}")

for word in words:
    if word == search_word:
        print(f"Found '{search_word}'!")
        break
else:
    print(f"'{search_word}' not found in list.")
print()


# ============================================================================
# QUICK CHALLENGES
# ============================================================================

print("=== CHALLENGES ===")
print("1) Write a loop that prints numbers 1-20 but skips multiples of 4.")
print("2) Create a program that finds the first even number in a list.")
print("3) Write a loop that breaks when the sum exceeds 100.")
print("4) Create a countdown that stops at 5.")
print("5) Find a specific character in a string using break.")
print("6) Skip words shorter than 5 characters in a list.")
print("7) Write a loop with else that prints 'Not found' if item not in list.")
print("\nTry implementing these!\n")

print("=== END OF BREAK/CONTINUE EXAMPLES ===")
