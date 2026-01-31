
# Python Basics – Complete Guide

This module covers the fundamental concepts needed to start programming in Python.

---

## 1. Hello World

### What is "Hello World"?
The "Hello World" program is the simplest program you can write. It simply prints the text "Hello World" to the screen. It's traditionally used to verify that your programming environment is set up correctly.

### The `print()` Function
```python
print("Hello World")
```
- `print()` is a built-in Python function that outputs text to the console
- Text must be enclosed in quotes (single or double)
- Each `print()` statement creates a new line

### Key Concepts:
- **Functions**: Reusable blocks of code that perform specific tasks
- **Output**: Displaying information to the user
- **Console/Terminal**: Where output is displayed

---

## 2. Variables

### What is a Variable?
A variable is a named container that stores a value. Think of it as a box labeled with a name where you can store information for later use.

### Creating Variables
```python
name = "John"
age = 25
height = 5.9
```

### Naming Rules:
- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Cannot contain spaces
- Are case-sensitive (`name` and `Name` are different)
- Cannot be Python keywords (like `if`, `for`, `while`)
- Use descriptive names (e.g., `user_age` instead of `a`)

### Naming Conventions:
- **snake_case**: `first_name` (preferred in Python)
- **camelCase**: `firstName`
- **PascalCase**: `FirstName`

### Reassigning Variables
```python
x = 10
x = 20  # x now holds 20, not 10
```
Variables can be changed at any time.

### Multiple Assignment
```python
a, b, c = 1, 2, 3
x = y = z = 0  # All three variables equal 0
```

---

## 3. Data Types

Before working with Python variables, it's important to understand data types. A data type describes the kind of value a variable holds. For example, a number, a piece of text, or a list of items. Programming languages use data types so they know how to store and work with different kinds of information.

Python is a dynamically-typed language like JavaScript, meaning you don't need to explicitly declare types for variables. The language knows what data type a variable is based on what you assign to it.

### Primary Data Types:

#### **Integer (int)**
- Whole numbers without decimals
- Can be positive or negative
```python
age = 25
temperature = -5
year = 2024
```

#### **Float (float)**
- Numbers with decimals
- Used for precise measurements
```python
price = 19.99
height = 5.8
pi = 3.14159
```

#### **String (str)**
- Text data enclosed in quotes (single or double)
- Immutable (cannot be changed after creation)
```python
name = "Alice"
city = 'New York'
message = "Hello, World!"
```

#### **Boolean (bool)**
- Only two possible values: `True` or `False`
- Used in conditional logic
```python
is_student = True
is_admin = False
```

#### **None**
- Represents the absence of a value
- Used as a placeholder
```python
result = None
```

### Checking Data Types
Use the `type()` function to check what type a variable is:
```python
type(25)        # <class 'int'>
type(25.5)      # <class 'float'>
type("Hello")   # <class 'str'>
type(True)      # <class 'bool'>
type(None)      # <class 'NoneType'>
```

---

## 4. Type Casting

Type casting is the process of converting a value from one data type to another. This is useful when you need to change how Python interprets a value.

### Common Type Casting Functions:

#### **int() – Convert to Integer**
- Removes decimal points from floats
- Converts strings containing numbers to integers
```python
int(25.7)       # Output: 25
int("50")       # Output: 50
int(True)       # Output: 1
int(False)      # Output: 0
```
⚠️ **Note**: `int("25.5")` will cause an error. Remove the decimal first.

#### **float() – Convert to Float**
- Adds decimal points to integers
- Converts strings containing numbers to floats
```python
float(25)       # Output: 25.0
float("3.14")   # Output: 3.14
float(True)     # Output: 1.0
```

#### **str() – Convert to String**
- Converts any value to text format
- Useful for combining different data types
```python
str(25)         # Output: "25"
str(3.14)       # Output: "3.14"
str(True)       # Output: "True"
```

#### **bool() – Convert to Boolean**
- Converts values to True or False
- Most values are `True` except: 0, 0.0, "", None, False
```python
bool(1)         # Output: True
bool(0)         # Output: False
bool("Hello")   # Output: True
bool("")        # Output: False
bool(None)      # Output: False
```

### Practical Examples:
```python
# User input is always a string, so we cast it to int for calculations
age_input = input("Enter your age: ")  # User enters "25"
age = int(age_input)                    # Convert to integer

# Combining different types using str()
name = "Alice"
age = 30
message = "My name is " + name + " and I am " + str(age) + " years old"
print(message)  # Output: My name is Alice and I am 30 years old
```

### Implicit vs Explicit Casting:
- **Implicit**: Python automatically converts types (rare in basic operations)
- **Explicit**: You explicitly convert using functions like `int()`, `float()`, `str()`

---

## Summary Table

| Data Type | Example | Description |
|-----------|---------|-------------|
| int | 25, -5, 0 | Whole numbers |
| float | 3.14, -2.5 | Decimal numbers |
| str | "Hello", 'World' | Text data |
| bool | True, False | True/False values |
| None | None | No value/null |

---

## Best Practices:
1. Use descriptive variable names that explain the purpose
2. Use consistent naming conventions (snake_case in Python)
3. Understand your data types to avoid errors
4. Cast types explicitly when needed to prevent confusion
5. Use `type()` to debug and understand variable types

---

## Common Errors to Avoid:
- ❌ `x = 10 + "5"` – Can't add int and str (TypeError)
- ❌ `name = Alice` – Missing quotes around string
- ✅ `name = "Alice"` – Correct: string in quotes
- ❌ `int("25.5")` – Can't convert string with decimal directly
- ✅ `int(float("25.5"))` – Correct: convert to float first, then int