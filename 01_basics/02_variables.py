"""
Topic: 02_variables
Source: freeCodeCamp Python

This file demonstrates how to create, name, and use variables in Python.
Variables are containers for storing data values.
"""

# ============================================================================
# BASIC VARIABLE CREATION
# ============================================================================

print("=== BASIC VARIABLE CREATION ===\n")

# Creating simple variables
name = "Alice"
age = 25
height = 5.8
is_student = True

# Display the variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}")
print()


# ============================================================================
# VARIABLE NAMING CONVENTIONS
# ============================================================================

print("=== VARIABLE NAMING CONVENTIONS ===\n")

# Good variable names (snake_case - Python convention)
user_first_name = "John"
user_last_name = "Doe"
user_email_address = "john@example.com"
total_amount = 100.50

print(f"First Name: {user_first_name}")
print(f"Last Name: {user_last_name}")
print(f"Email: {user_email_address}")
print(f"Total: ${total_amount}")
print()


# ============================================================================
# REASSIGNING VARIABLES
# ============================================================================

print("=== REASSIGNING VARIABLES ===\n")

# Original value
score = 85
print(f"Original score: {score}")

# Reassign to a new value
score = 95
print(f"Updated score: {score}")

# Reassign by performing operations
score = score + 5
print(f"After adding 5: {score}")
print()


# ============================================================================
# MULTIPLE VARIABLE ASSIGNMENT
# ============================================================================

print("=== MULTIPLE VARIABLE ASSIGNMENT ===\n")

# Unpacking - assign multiple values at once
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Multiple variables with same value
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

# Swapping variables
p, q = 5, 15
print(f"Before swap: p={p}, q={q}")
p, q = q, p  # Swap values
print(f"After swap: p={p}, q={q}")
print()


# ============================================================================
# PRACTICE EXAMPLE 1: PERSONAL INFORMATION
# ============================================================================

print("=== PRACTICE 1: PERSONAL INFORMATION ===\n")

# Create variables for personal information
person_name = "Bob Smith"
person_age = 30
person_city = "New York"
person_occupation = "Software Engineer"
years_experience = 5

# Display the information
print(f"Name: {person_name}")
print(f"Age: {person_age} years old")
print(f"City: {person_city}")
print(f"Occupation: {person_occupation}")
print(f"Years of Experience: {years_experience} years")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: MATHEMATICAL CALCULATIONS
# ============================================================================

print("=== PRACTICE 2: MATHEMATICAL CALCULATIONS ===\n")

# Variables for a simple calculation
principal = 1000      # Initial amount
interest_rate = 0.05  # 5% annual interest
years = 2             # Time period

# Calculate simple interest
simple_interest = principal * interest_rate * years
final_amount = principal + simple_interest

print(f"Principal: ${principal}")
print(f"Interest Rate: {interest_rate * 100}%")
print(f"Years: {years}")
print(f"Simple Interest: ${simple_interest}")
print(f"Final Amount: ${final_amount}")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: ONLINE SHOPPING CART
# ============================================================================

print("=== PRACTICE 3: SHOPPING CART ===\n")

# Variables for items in shopping cart
item1_name = "Laptop"
item1_price = 999.99
item1_quantity = 1

item2_name = "Mouse"
item2_price = 29.99
item2_quantity = 2

# Calculate subtotals
item1_subtotal = item1_price * item1_quantity
item2_subtotal = item2_price * item2_quantity

# Calculate total
subtotal = item1_subtotal + item2_subtotal
tax = subtotal * 0.08  # 8% tax
total = subtotal + tax

# Display receipt
print("--- SHOPPING RECEIPT ---")
print(f"{item1_name}: ${item1_price} x {item1_quantity} = ${item1_subtotal}")
print(f"{item2_name}: ${item2_price} x {item2_quantity} = ${item2_subtotal}")
print(f"Subtotal: ${subtotal}")
print(f"Tax (8%): ${tax}")
print(f"Total: ${total}")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: STUDENT GRADES
# ============================================================================

print("=== PRACTICE 4: STUDENT GRADES ===\n")

# Student information and grades
student_name = "Emma"
math_grade = 95
english_grade = 87
science_grade = 92

# Calculate average
average_grade = (math_grade + english_grade + science_grade) / 3

print(f"Student: {student_name}")
print(f"Math: {math_grade}")
print(f"English: {english_grade}")
print(f"Science: {science_grade}")
print(f"Average: {average_grade:.2f}")
print()


# ============================================================================
# PRACTICE EXAMPLE 5: TIME CONVERSION
# ============================================================================

print("=== PRACTICE 5: TIME CONVERSION ===\n")

# Variables for time conversion
total_seconds = 3665  # Total seconds to convert

# Convert to hours, minutes, and seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Total Seconds: {total_seconds}")
print(f"Converted to: {hours}h {minutes}m {seconds}s")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: TEMPERATURE CONVERSION
# ============================================================================

print("=== PRACTICE 6: TEMPERATURE CONVERSION ===\n")

# Celsius to Fahrenheit conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

# Fahrenheit to Celsius conversion
fahrenheit2 = 77
celsius2 = (fahrenheit2 - 32) * 5/9

print(f"{fahrenheit2}°F = {celsius2:.2f}°C")
print()


# ============================================================================
# QUICK CHALLENGE: TRY IT YOURSELF
# ============================================================================

print("=== CHALLENGE: CREATE YOUR OWN VARIABLES ===\n")
print("Try creating variables for:")
print("1. Your favorite color")
print("2. Your favorite number")
print("3. Whether you like pizza (True/False)")
print("4. Your favorite book title")
print("\nThen print them out!\n")
