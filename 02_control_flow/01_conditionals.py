"""
Topic: 01_conditionals
Source: freeCodeCamp Python

This file demonstrates conditional statements (if, elif, else) for
controlling program flow based on conditions.
"""

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================

print("=== COMPARISON OPERATORS ===\n")

# Equal to (==)
print("Equal to (==):")
print(f"5 == 5: {5 == 5}")  # True
print(f"5 == 3: {5 == 3}")  # False

# Not equal to (!=)
print("\nNot equal to (!=):")
print(f"5 != 3: {5 != 3}")  # True
print(f"5 != 5: {5 != 5}")  # False

# Less than (<)
print("\nLess than (<):")
print(f"3 < 5: {3 < 5}")  # True
print(f"5 < 3: {5 < 3}")  # False

# Greater than (>)
print("\nGreater than (>):")
print(f"5 > 3: {5 > 3}")  # True
print(f"3 > 5: {3 > 5}")  # False

# Less than or equal (<=)
print("\nLess than or equal (<=):")
print(f"5 <= 5: {5 <= 5}")  # True
print(f"3 <= 5: {3 <= 5}")  # True

# Greater than or equal (>=)
print("\nGreater than or equal (>=):")
print(f"5 >= 5: {5 >= 5}")  # True
print(f"5 >= 3: {5 >= 3}")  # True
print()


# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

print("=== LOGICAL OPERATORS ===\n")

# and operator (both must be True)
print("and operator:")
print(f"True and True: {True and True}")  # True
print(f"True and False: {True and False}")  # False
print(f"False and False: {False and False}")  # False

# or operator (at least one must be True)
print("\nor operator:")
print(f"True or False: {True or False}")  # True
print(f"False or False: {False or False}")  # False
print(f"True or True: {True or True}")  # True

# not operator (reverses boolean)
print("\nnot operator:")
print(f"not True: {not True}")  # False
print(f"not False: {not False}")  # True
print()


# ============================================================================
# BASIC IF STATEMENT
# ============================================================================

print("=== BASIC IF STATEMENT ===\n")

age = 20

if age >= 18:
    print("You are an adult.")
print()


# ============================================================================
# IF...ELSE STATEMENT
# ============================================================================

print("=== IF...ELSE STATEMENT ===\n")

score = 45

if score >= 50:
    print("You passed!")
else:
    print("You failed. Try again.")
print()


# ============================================================================
# IF...ELIF...ELSE STATEMENT
# ============================================================================

print("=== IF...ELIF...ELSE STATEMENT ===\n")

grade_score = 85

if grade_score >= 90:
    grade = "A"
    print("Excellent!")
elif grade_score >= 80:
    grade = "B"
    print("Good job!")
elif grade_score >= 70:
    grade = "C"
    print("Satisfactory.")
elif grade_score >= 60:
    grade = "D"
    print("Passing, but needs improvement.")
else:
    grade = "F"
    print("Failed.")

print(f"Your grade is: {grade}")
print()


# ============================================================================
# NESTED IF STATEMENTS
# ============================================================================

print("=== NESTED IF STATEMENTS ===\n")

age = 25
has_license = True

if age >= 18:
    print("You are 18 or older.")
    
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a driver's license.")
else:
    print("You are too young to drive.")
print()


# ============================================================================
# PRACTICE EXAMPLE 1: TEMPERATURE CHECK
# ============================================================================

print("=== PRACTICE 1: TEMPERATURE CLASSIFICATION ===\n")

temperature = 25

if temperature < 0:
    weather = "Freezing"
elif temperature < 10:
    weather = "Cold"
elif temperature < 20:
    weather = "Cool"
elif temperature < 30:
    weather = "Warm"
else:
    weather = "Hot"

print(f"Temperature: {temperature}°C")
print(f"Weather: {weather}")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: LOGIN SYSTEM
# ============================================================================

print("=== PRACTICE 2: LOGIN SYSTEM ===\n")

correct_username = "john_doe"
correct_password = "secure123"

username = "john_doe"
password = "secure123"

if username == correct_username and password == correct_password:
    print("Login successful! Welcome, john_doe.")
elif username == correct_username:
    print("Username correct, but password is wrong.")
else:
    print("Username not found.")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: ELIGIBILITY CHECK
# ============================================================================

print("=== PRACTICE 3: VOTING ELIGIBILITY ===\n")

age = 20
is_citizen = True

if age >= 18 and is_citizen:
    print("You are eligible to vote!")
elif age < 18:
    print("You are too young to vote.")
else:
    print("You must be a citizen to vote.")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: DISCOUNT CALCULATION
# ============================================================================

print("=== PRACTICE 4: DISCOUNT PRICING ===\n")

purchase_amount = 150
is_member = True

print(f"Original price: ${purchase_amount}")

if is_member and purchase_amount >= 100:
    discount = purchase_amount * 0.20  # 20% discount
    final_price = purchase_amount - discount
    print(f"Member discount (20%): -${discount}")
    print(f"Final price: ${final_price}")
elif is_member:
    discount = purchase_amount * 0.10  # 10% discount
    final_price = purchase_amount - discount
    print(f"Member discount (10%): -${discount}")
    print(f"Final price: ${final_price}")
else:
    print(f"Final price: ${purchase_amount}")
print()


# ============================================================================
# PRACTICE EXAMPLE 5: EVEN/ODD CHECKER
# ============================================================================

print("=== PRACTICE 5: EVEN/ODD CHECKER ===\n")

numbers = [12, 25, 30, 17, 44]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: BMI CALCULATOR
# ============================================================================

print("=== PRACTICE 6: BMI CATEGORY ===\n")

weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)

print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")
print()


# ============================================================================
# PRACTICE EXAMPLE 7: DAY OF WEEK
# ============================================================================

print("=== PRACTICE 7: WEEKEND OR WEEKDAY ===\n")

day = "Saturday"

if day in ["Saturday", "Sunday"]:
    print(f"{day} is a weekend day!")
    print("Enjoy your day off!")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(f"{day} is a weekday.")
    print("Time to work!")
else:
    print("Invalid day.")
print()


# ============================================================================
# PRACTICE EXAMPLE 8: STUDENT PASS/FAIL
# ============================================================================

print("=== PRACTICE 8: STUDENT GRADING ===\n")

students = [
    ("Alice", 95),
    ("Bob", 72),
    ("Charlie", 58),
    ("Diana", 88),
]

print("Student Report:")
print("-" * 30)

for name, score in students:
    if score >= 80:
        status = "Passed - Excellent"
    elif score >= 70:
        status = "Passed - Good"
    elif score >= 60:
        status = "Passed - Acceptable"
    else:
        status = "Failed - Retake Required"
    
    print(f"{name:<12} {score:>3} → {status}")
print()


# ============================================================================
# PRACTICE EXAMPLE 9: NUMBER RANGE CHECK
# ============================================================================

print("=== PRACTICE 9: NUMBER RANGE CHECK ===\n")

test_numbers = [5, 15, 25, 35, 45, 55]

for num in test_numbers:
    if 0 <= num < 10:
        range_label = "0-9"
    elif 10 <= num < 20:
        range_label = "10-19"
    elif 20 <= num < 30:
        range_label = "20-29"
    elif 30 <= num < 40:
        range_label = "30-39"
    elif 40 <= num < 50:
        range_label = "40-49"
    else:
        range_label = "50+"
    
    print(f"{num} is in range {range_label}")
print()


# ============================================================================
# PRACTICE EXAMPLE 10: MOVIE RATING
# ============================================================================

print("=== PRACTICE 10: MOVIE RATING RECOMMENDATION ===\n")

age = 16

if age < 5:
    print("Recommended rating: G (General Audiences)")
elif age < 13:
    print("Recommended rating: PG (Parental Guidance)")
elif age < 17:
    print("Recommended rating: PG-13 (Parents Strongly Cautioned)")
else:
    print("You can watch any rating including R and NC-17")
print()


# ============================================================================
# TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ============================================================================

print("=== TERNARY OPERATOR ===\n")

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

score = 75
result = "Pass" if score >= 60 else "Fail"
print(f"Score {score}: {result}")

num = 7
parity = "even" if num % 2 == 0 else "odd"
print(f"Number {num}: {parity}")
print()


# ============================================================================
# QUICK CHALLENGES
# ============================================================================

print("=== CHALLENGES ===")
print("1) Create a program that determines if a number is positive, negative, or zero.")
print("2) Check if a year is a leap year (divisible by 4, except centuries divisible by 400).")
print("3) Compare three numbers and find the largest one.")
print("4) Check if a character is a vowel or consonant.")
print("5) Create a simple rock-paper-scissors game with conditionals.")
print("\nTry implementing these!\n")

print("=== END OF CONDITIONALS EXAMPLES ===")
