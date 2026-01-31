"""
Topic: 03_data_types
Source: freeCodeCamp Python

This file demonstrates all the primary data types in Python:
- Integer (int)
- Float (float)
- String (str)
- Boolean (bool)
- None
"""

# ============================================================================
# INTEGER (int) - WHOLE NUMBERS
# ============================================================================

print("=== INTEGER DATA TYPE ===\n")

# Positive integers
age = 25
year = 2024
population = 8000000000

print(f"Age: {age}")
print(f"Year: {year}")
print(f"Population: {population}")

# Negative integers
temperature = -15
debt = -500

print(f"Temperature: {temperature}°C")
print(f"Debt: ${debt}")

# Zero
balance = 0
print(f"Balance: {balance}")

# Check the type
print(f"Type of age: {type(age)}")
print()


# ============================================================================
# FLOAT - DECIMAL NUMBERS
# ============================================================================

print("=== FLOAT DATA TYPE ===\n")

# Basic floats
price = 19.99
height = 5.9
pi = 3.14159

print(f"Price: ${price}")
print(f"Height: {height} feet")
print(f"Pi: {pi}")

# Negative floats
temperature_celsius = -10.5
discount = -5.25

print(f"Temperature: {temperature_celsius}°C")
print(f"Discount: {discount}%")

# Scientific notation
very_large = 1.5e6  # 1.5 million
very_small = 2.5e-4  # 0.00025

print(f"Very Large Number: {very_large}")
print(f"Very Small Number: {very_small}")

# Check the type
print(f"Type of price: {type(price)}")
print()


# ============================================================================
# STRING - TEXT DATA
# ============================================================================

print("=== STRING DATA TYPE ===\n")

# Single and double quotes
name = "Alice"
greeting = 'Hello, World!'

print(f"Name: {name}")
print(f"Greeting: {greeting}")

# Multi-line strings
message = """
This is a multi-line string.
It can span multiple lines.
Useful for longer text!
"""
print("Message:")
print(message)

# Empty string
empty = ""
print(f"Empty string: '{empty}' (length: {len(empty)})")

# Strings with numbers (still strings, not integers!)
phone = "555-1234"
zip_code = "10001"

print(f"Phone: {phone}")
print(f"Zip Code: {zip_code}")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(f"Full Name: {full_name}")

# Check the type
print(f"Type of name: {type(name)}")
print()


# ============================================================================
# BOOLEAN - TRUE/FALSE VALUES
# ============================================================================

print("=== BOOLEAN DATA TYPE ===\n")

# Boolean values
is_student = True
is_admin = False
has_license = True

print(f"Is Student: {is_student}")
print(f"Is Admin: {is_admin}")
print(f"Has License: {has_license}")

# Comparison results return booleans
is_greater = 10 > 5  # True
is_equal = "hello" == "world"  # False

print(f"10 > 5: {is_greater}")
print(f"'hello' == 'world': {is_equal}")

# Check the type
print(f"Type of is_student: {type(is_student)}")
print()


# ============================================================================
# NONE - ABSENCE OF VALUE
# ============================================================================

print("=== NONE DATA TYPE ===\n")

# None represents the absence of a value
result = None
empty_value = None

print(f"Result: {result}")
print(f"Empty Value: {empty_value}")

# Check the type
print(f"Type of result: {type(result)}")
print()


# ============================================================================
# CHECKING DATA TYPES WITH type()
# ============================================================================

print("=== CHECKING DATA TYPES ===\n")

# Create variables of different types
my_int = 42
my_float = 3.14
my_string = "Python"
my_bool = True
my_none = None

# Check each type
print(f"type({my_int}) = {type(my_int)}")
print(f"type({my_float}) = {type(my_float)}")
print(f"type({my_string}) = {type(my_string)}")
print(f"type({my_bool}) = {type(my_bool)}")
print(f"type({my_none}) = {type(my_none)}")
print()


# ============================================================================
# PRACTICE EXAMPLE 1: PRODUCT INFORMATION
# ============================================================================

print("=== PRACTICE 1: PRODUCT INFORMATION ===\n")

product_name = "Laptop"      # String
product_price = 999.99       # Float
quantity_in_stock = 15       # Integer
is_available = True          # Boolean
discount_price = None        # None (no discount yet)

print(f"Product: {product_name}")
print(f"Price: ${product_price}")
print(f"In Stock: {quantity_in_stock} units")
print(f"Available: {is_available}")
print(f"Discount Price: {discount_price}")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: EMPLOYEE DETAILS
# ============================================================================

print("=== PRACTICE 2: EMPLOYEE DETAILS ===\n")

employee_name = "Sarah Johnson"      # String
employee_id = 10045                  # Integer
hourly_rate = 25.50                  # Float
is_full_time = True                  # Boolean
department = "Engineering"           # String
years_employed = 3                   # Integer

print(f"Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Hourly Rate: ${hourly_rate}")
print(f"Full-time: {is_full_time}")
print(f"Department: {department}")
print(f"Years Employed: {years_employed}")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: WEBSITE USER ACCOUNT
# ============================================================================

print("=== PRACTICE 3: USER ACCOUNT ===\n")

username = "john_doe"                # String
email = "john@example.com"           # String
user_id = 12345                      # Integer
account_balance = 150.75             # Float
is_verified = True                   # Boolean
is_premium = False                   # Boolean
last_login = None                    # None (hasn't logged in yet)

print(f"Username: {username}")
print(f"Email: {email}")
print(f"User ID: {user_id}")
print(f"Account Balance: ${account_balance}")
print(f"Verified: {is_verified}")
print(f"Premium Member: {is_premium}")
print(f"Last Login: {last_login}")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: SCHOOL INFORMATION
# ============================================================================

print("=== PRACTICE 4: SCHOOL INFORMATION ===\n")

school_name = "Lincoln High School"  # String
total_students = 1250                # Integer
student_teacher_ratio = 15.5         # Float
is_public = True                     # Boolean
founded_year = 1985                  # Integer
school_code = "LHS-001"              # String

print(f"School: {school_name}")
print(f"Total Students: {total_students}")
print(f"Student-Teacher Ratio: {student_teacher_ratio}:1")
print(f"Public School: {is_public}")
print(f"Founded: {founded_year}")
print(f"School Code: {school_code}")
print()


# ============================================================================
# PRACTICE EXAMPLE 5: MIXED DATA TYPES
# ============================================================================

print("=== PRACTICE 5: MIXED DATA TYPES ===\n")

# Create a comprehensive example mixing all types
item_name = "Smartphone"             # String
item_price = 599.99                  # Float
quantity = 2                         # Integer
is_in_stock = True                   # Boolean
warranty_info = None                 # None

# Calculate total
total_cost = item_price * quantity

print(f"Item: {item_name}")
print(f"Unit Price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"In Stock: {is_in_stock}")
print(f"Warranty: {warranty_info}")
print(f"Total Cost: ${total_cost}")
print()


# ============================================================================
# PRACTICAL TIPS
# ============================================================================

print("=== PRACTICAL TIPS ===\n")

# Tip 1: String numbers are not integers
phone = "555-1234"  # This is a string, not a number
print(f"Phone (string): {phone}, type: {type(phone)}")

# Tip 2: Check if a boolean condition is true
is_raining = True
if is_raining:
    print("Bring an umbrella!")

# Tip 3: Use None as a placeholder
future_value = None
print(f"Future value will be set later: {future_value}")

# Tip 4: Floats can have precision issues
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # May not be exactly 0.3

print("\n=== END OF DATA TYPES EXAMPLES ===")
