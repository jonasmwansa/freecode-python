"""
Topic: 04_type_casting
Source: freeCodeCamp Python

This file demonstrates conversion between common Python types
and practical examples showing when and how to cast safely.
"""

print("=== TYPE CASTING EXAMPLES ===\n")


# ---------------------------------------------------------------------------
# BASIC CASTS: int(), float(), str(), bool()
# ---------------------------------------------------------------------------

print("-- Basic conversions --")

# int from float (truncates toward zero)
val = 7.9
print(f"int({val}) -> {int(val)}")

# float from int
val_i = 10
print(f"float({val_i}) -> {float(val_i)}")

# str from numbers
num = 42
print(f"str({num}) -> '{str(num)}'")

# bool conversions: empty/zero values are False
print(f"bool(0) -> {bool(0)}")
print(f"bool(1) -> {bool(1)}")
print(f"bool('') -> {bool('')} (empty string is False)")
print(f"bool('hello') -> {bool('hello')}\n")


# ---------------------------------------------------------------------------
# COMMON PITFALLS
# ---------------------------------------------------------------------------

print("-- Common pitfalls --")

# Converting string that contains a decimal directly to int raises ValueError
s = "25.5"
print(f"s = '{s}'")
try:
	print("int(s) ->", int(s))
except ValueError as e:
	print("int(s) raises:", e)

# Correct approach: convert to float first, then to int (if appropriate)
print("int(float(s)) ->", int(float(s)))

# Converting non-numeric strings to int/float also raises errors
bad = "abc"
try:
	print("int('abc') ->", int(bad))
except ValueError as e:
	print("int('abc') raises:", e)

print()


# ---------------------------------------------------------------------------
# USER INPUT EXAMPLE (safe casting)
# ---------------------------------------------------------------------------

print("-- User input example --")

def safe_int_input(prompt: str, default: int = 0) -> int:
	"""Prompt the user and return an int, falling back to default on error."""
	try:
		raw = input(prompt)
		return int(raw)
	except Exception:
		print("Invalid input, using default:", default)
		return default

# Example usage (comment out when running automated tests)
# age = safe_int_input("Enter your age: ")
# print("You entered age:", age)

print("(safe_int_input example included but commented to avoid blocking scripts)\n")


# ---------------------------------------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------------------------------------

print("-- Practical examples --")

# 1) Concatenate number with string using str()
count = 3
message = "You have " + str(count) + " new messages."
print(message)

# 2) Calculate total from string inputs (common when reading CSV/JSON)
price_str = "19.99"
qty_str = "3"
total = float(price_str) * int(qty_str)
print(f"Total from strings: ${total}")

# 3) Use bool to interpret toggles
flag_str = ""  # imagine reading from a config
is_enabled = bool(flag_str)
print(f"Flag string '{flag_str}' -> is_enabled = {is_enabled}")

print()


# ---------------------------------------------------------------------------
# QUICK CHALLENGES (try these)
# ---------------------------------------------------------------------------

print("=== CHALLENGES ===")
print("1) Convert the string '100' to an int and add 50.")
year = int("100") + 50
print(year)

print("2) Safely convert '3.14' to an int by rounding when appropriate.")
val = 3.14
rounded = round(val)
print(f"Rounded {val} -> {rounded}")

print("3) Given a list of numeric strings, compute their float sum.")

numeric_strings = ["1.5", "2.7", "3.3"]
total = sum(float(s) for s in numeric_strings)
print(f"Sum of {numeric_strings} = {total}")

print("\nTry implementing these in your editor to practice casts!\n")

print("=== END OF TYPE CASTING EXAMPLES ===")

