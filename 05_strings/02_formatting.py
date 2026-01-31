"""
Topic: 02_formatting
Source: freeCodeCamp Python

This file demonstrates different string formatting techniques in Python.
From old-style % formatting to modern f-strings.
"""

# ============================================================================
# F-STRINGS (Python 3.6+) - RECOMMENDED
# ============================================================================

print("=== F-STRINGS (MODERN & PREFERRED) ===\n")

# Basic f-string
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")

# Expressions in f-strings
x = 10
y = 20
print(f"Sum of {x} and {y} is {x + y}")

# Calling methods in f-strings
text = "hello"
print(f"Uppercase: {text.upper()}")

# F-strings with format specifiers
pi = 3.14159
print(f"Pi: {pi}")
print(f"Pi rounded: {pi:.2f}")  # 2 decimal places
print(f"Pi in percent: {pi:.1%}")  # As percentage

# Width and alignment
value = "Python"
print(f"Left align: '{value:<15}'")  # 15 chars, left-aligned
print(f"Right align: '{value:>15}'")  # 15 chars, right-aligned
print(f"Center: '{value:^15}'")  # 15 chars, centered

# Padding with zeros
num = 42
print(f"Zero-padded: {num:05d}")  # Pad to 5 digits with zeros
print()


# ============================================================================
# STR.FORMAT() METHOD (Python 3+)
# ============================================================================

print("=== STR.FORMAT() METHOD ===\n")

# Basic usage with positional arguments
print("{} is {} years old".format("Bob", 25))

# Using index numbers
print("{0} is {1} years old, {0} loves {2}".format("Bob", 25, "coding"))

# Using keyword arguments
print("{name} is {age} years old".format(name="Charlie", age=35))

# Format specifiers
price = 19.999
print("Price: ${:.2f}".format(price))

# Width and alignment
print("Left: '{:<10}' | Right: '{:>10}' | Center: '{:^10}'".format("Hi", "Hi", "Hi"))

# Zero padding
print("Code: {:05d}".format(123))
print()


# ============================================================================
# OLD-STYLE % FORMATTING (FOR LEGACY CODE)
# ============================================================================

print("=== OLD-STYLE % FORMATTING ===\n")

# String formatting
print("Name: %s, Age: %d" % ("Diana", 28))

# Multiple values
print("Values: %d, %.2f, %s" % (42, 3.14159, "hello"))

# Padding
print("Number: %05d" % 123)
print()


# ============================================================================
# PRACTICE EXAMPLE 1: INVOICE FORMATTING
# ============================================================================

print("=== PRACTICE 1: INVOICE ===\n")

item_name = "Laptop"
item_price = 999.99
quantity = 2
tax_rate = 0.08

subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("INVOICE")
print("-" * 40)
print(f"Item: {item_name}")
print(f"Unit Price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print("-" * 40)
print(f"Total: ${total:.2f}")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: DATA TABLE FORMATTING
# ============================================================================

print("=== PRACTICE 2: DATA TABLE ===\n")

# Student grades
students = [
    ("Alice", 95, 87, 92),
    ("Bob", 88, 91, 85),
    ("Charlie", 92, 89, 94),
]

# Header
print(f"{'Name':<12} {'Math':>6} {'English':>8} {'Science':>8}")
print("-" * 40)

# Data rows
for name, math, english, science in students:
    average = (math + english + science) / 3
    print(f"{name:<12} {math:>6} {english:>8} {science:>8}")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: CURRENCY FORMATTING
# ============================================================================

print("=== PRACTICE 3: CURRENCY FORMATTING ===\n")

amounts = [10, 100.5, 1234.567, 0.99]

print("Currency Formatting Examples:")
for amount in amounts:
    # Different format options
    print(f"${amount:>10.2f}")  # Right-aligned, 2 decimals

print("\nWith thousands separator:")
for amount in amounts:
    print(f"${amount:>12,.2f}")  # With comma separator
print()


# ============================================================================
# PRACTICE EXAMPLE 4: ALIGNMENT AND WIDTH
# ============================================================================

print("=== PRACTICE 4: ALIGNMENT ===\n")

items = ["Apple", "Banana", "Cherry"]
prices = [0.99, 1.29, 2.49]

print("Left-aligned items:")
for item, price in zip(items, prices):
    print(f"{item:<15} ${price:.2f}")

print("\nRight-aligned items:")
for item, price in zip(items, prices):
    print(f"{item:>15} ${price:>7.2f}")

print("\nCentered items:")
for item in items:
    print(f"{item:^20}")
print()


# ============================================================================
# PRACTICE EXAMPLE 5: PERCENTAGE FORMATTING
# ============================================================================

print("=== PRACTICE 5: PERCENTAGE FORMATTING ===\n")

# Test scores
test_score = 85
total_points = 100
percentage = test_score / total_points

print(f"Score: {test_score}/{total_points}")
print(f"Percentage: {percentage:.1%}")

# Multiple percentages
results = {"Math": 0.92, "English": 0.87, "Science": 0.95}

print("\nClass Results:")
for subject, percent in results.items():
    print(f"{subject:<15} {percent:.1%}")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: DATE AND TIME FORMATTING
# ============================================================================

print("=== PRACTICE 6: NUMBER FORMATTING ===\n")

# Large numbers
population = 8000000000
print(f"World population: {population:,}")  # With comma separator
print(f"Formatted: {population:_}")  # With underscore separator

# Hexadecimal, binary, octal
num = 255
print(f"\nNumber: {num}")
print(f"Hex: {num:x}")  # Lowercase hex
print(f"Hex: {num:X}")  # Uppercase hex
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print()


# ============================================================================
# PRACTICE EXAMPLE 7: SCIENTIFIC NOTATION
# ============================================================================

print("=== PRACTICE 7: SCIENTIFIC NOTATION ===\n")

large_num = 1234567.89
small_num = 0.00012345

print(f"Standard: {large_num}")
print(f"Scientific: {large_num:e}")  # lowercase e
print(f"Scientific: {large_num:.2e}")  # With precision

print(f"\nSmall number: {small_num}")
print(f"Scientific: {small_num:e}")
print()


# ============================================================================
# PRACTICE EXAMPLE 8: TEMPLATE-LIKE FORMATTING
# ============================================================================

print("=== PRACTICE 8: TEMPLATE FORMATTING ===\n")

person = {"name": "Emma", "age": 26, "city": "New York"}

# Using format with keyword arguments
message = "{name} is {age} years old and lives in {city}".format(**person)
print(message)

# Using f-string with dictionary unpacking
print(f"{person['name']} works in {person['city']}")

# Building a profile
profile_template = """
Name: {name}
Age: {age}
City: {city}
"""
print(profile_template.format(**person))
print()


# ============================================================================
# PRACTICE EXAMPLE 9: PADDING AND BORDERS
# ============================================================================

print("=== PRACTICE 9: BORDERS ===\n")

title = "Welcome"
width = 30

# Top border
print("=" * width)

# Centered title
print(f"{title:^{width}}")

# Separator
print("-" * width)

# Content
lines = ["This is line 1", "This is line 2", "This is line 3"]
for line in lines:
    print(f"| {line:<{width-4}} |")

# Bottom border
print("=" * width)
print()


# ============================================================================
# PRACTICE EXAMPLE 10: COMPARISON OF FORMATTING METHODS
# ============================================================================

print("=== PRACTICE 10: FORMATTING METHODS COMPARISON ===\n")

first_name = "John"
last_name = "Doe"
age = 35

print("1. F-string (recommended):")
print(f"{first_name} {last_name} is {age} years old")

print("\n2. str.format():")
print("{} {} is {} years old".format(first_name, last_name, age))

print("\n3. Old-style % formatting:")
print("%s %s is %d years old" % (first_name, last_name, age))

print("\n4. String concatenation:")
print(first_name + " " + last_name + " is " + str(age) + " years old")
print()


# ============================================================================
# QUICK CHALLENGES
# ============================================================================

print("=== CHALLENGES ===")
print("1) Format a price with currency symbol and 2 decimal places.")
print("2) Create a table with headers and data rows (aligned columns).")
print("3) Display a number in binary, hexadecimal, and octal formats.")
print("4) Format a percentage to show one decimal place.")
print("5) Create a greeting with name and age using each formatting method.")
print("\nTry implementing these!\n")

print("=== END OF FORMATTING EXAMPLES ===")
