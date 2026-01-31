"""
Topic: 01_string_methods
Source: freeCodeCamp Python

This file demonstrates common string methods used for text manipulation,
searching, and transformation in Python.
"""

# ============================================================================
# CASE CONVERSION METHODS
# ============================================================================

print("=== CASE CONVERSION METHODS ===\n")

text = "Hello, World!"

# upper() - Convert to uppercase
print(f"Original: {text}")
print(f"upper(): {text.upper()}")

# lower() - Convert to lowercase
print(f"lower(): {text.lower()}")

# title() - Capitalize first letter of each word
print(f"title(): {text.title()}")

# capitalize() - Capitalize first letter only
phrase = "python is awesome"
print(f"capitalize(): {phrase.capitalize()}")

# swapcase() - Swap uppercase and lowercase
print(f"swapcase(): {text.swapcase()}")
print()


# ============================================================================
# WHITESPACE MANIPULATION
# ============================================================================

print("=== WHITESPACE MANIPULATION ===\n")

dirty = "  Hello, Python!  \n"

# strip() - Remove leading and trailing whitespace
print(f"Original: '{dirty}'")
print(f"strip(): '{dirty.strip()}'")

# lstrip() - Remove leading whitespace only
print(f"lstrip(): '{dirty.lstrip()}'")

# rstrip() - Remove trailing whitespace only
print(f"rstrip(): '{dirty.rstrip()}'")

# You can specify characters to remove
text_with_chars = "***Hello***"
print(f"Original: {text_with_chars}")
print(f"strip('*'): {text_with_chars.strip('*')}")
print()


# ============================================================================
# FINDING AND SEARCHING
# ============================================================================

print("=== FINDING AND SEARCHING ===\n")

sentence = "The quick brown fox jumps over the lazy dog"

# find() - Find index of substring (returns -1 if not found)
print(f"Text: {sentence}")
print(f"find('brown'): {sentence.find('brown')}")
print(f"find('xyz'): {sentence.find('xyz')}")

# rfind() - Find from the right (last occurrence)
text2 = "apple apple banana apple"
print(f"Text: {text2}")
print(f"find('apple'): {text2.find('apple')}")
print(f"rfind('apple'): {text2.rfind('apple')}")

# index() - Like find(), but raises error if not found
print(f"index('quick'): {sentence.index('quick')}")
try:
    sentence.index('xyz')
except ValueError as e:
    print(f"index('xyz') raises: {e}")

# count() - Count occurrences of substring
print(f"count('the'): {sentence.count('the')}")
print()


# ============================================================================
# CHECKING CONTENT
# ============================================================================

print("=== CHECKING CONTENT ===\n")

# startswith() - Check if string starts with substring
url = "https://www.example.com"
print(f"URL: {url}")
print(f"startswith('https'): {url.startswith('https')}")
print(f"startswith('http'): {url.startswith('http')}")

# endswith() - Check if string ends with substring
filename = "document.pdf"
print(f"Filename: {filename}")
print(f"endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"endswith('.txt'): {filename.endswith('.txt')}")

# isdigit() - Check if all characters are digits
print(f"isdigit('12345'): {'12345'.isdigit()}")
print(f"isdigit('123a5'): {'123a5'.isdigit()}")

# isalpha() - Check if all characters are letters
print(f"isalpha('hello'): {'hello'.isalpha()}")
print(f"isalpha('hello123'): {'hello123'.isalpha()}")

# isalnum() - Check if all characters are alphanumeric
print(f"isalnum('hello123'): {'hello123'.isalnum()}")
print(f"isalnum('hello 123'): {'hello 123'.isalnum()}")

# isspace() - Check if all characters are whitespace
print(f"isspace('   '): {'   '.isspace()}")
print(f"isspace('a  '): {'a  '.isspace()}")

# islower() / isupper() - Check case
print(f"islower('hello'): {'hello'.islower()}")
print(f"isupper('HELLO'): {'HELLO'.isupper()}")
print()


# ============================================================================
# REPLACING AND SUBSTITUTION
# ============================================================================

print("=== REPLACING AND SUBSTITUTION ===\n")

# replace() - Replace all occurrences
original = "Python is great. Python is fun."
print(f"Original: {original}")
replaced = original.replace("Python", "Java")
print(f"replace('Python', 'Java'): {replaced}")

# Replace with limit (count parameter)
limited = original.replace("Python", "Java", 1)
print(f"replace('Python', 'Java', 1): {limited}")

# Remove by replacing with empty string
text_to_clean = "H-e-l-l-o"
print(f"Original: {text_to_clean}")
print(f"remove hyphens: {text_to_clean.replace('-', '')}")
print()


# ============================================================================
# SPLITTING AND JOINING
# ============================================================================

print("=== SPLITTING AND JOINING ===\n")

# split() - Split string into list
csv_data = "apple,banana,orange,grape"
print(f"Original: {csv_data}")
items = csv_data.split(',')
print(f"split(','): {items}")

# split with no argument (splits on whitespace)
sentence = "The quick brown fox"
words = sentence.split()
print(f"Original: {sentence}")
print(f"split(): {words}")

# splitlines() - Split on newlines
multiline = "Line one\nLine two\nLine three"
print(f"Original: {repr(multiline)}")
lines = multiline.splitlines()
print(f"splitlines(): {lines}")

# join() - Join list into string
print(f"join(items): {', '.join(items)}")
print(f"join(words): {' | '.join(words)}")
print()


# ============================================================================
# PRACTICE EXAMPLE 1: USER EMAIL VALIDATION
# ============================================================================

print("=== PRACTICE 1: EMAIL PROCESSING ===\n")

email = "  JOHN.DOE@EXAMPLE.COM  "

# Clean and process email
email_cleaned = email.strip().lower()
print(f"Original: '{email}'")
print(f"Cleaned: '{email_cleaned}'")

# Check if valid format
is_valid = '@' in email_cleaned and '.' in email_cleaned
print(f"Contains @ and .: {is_valid}")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: TEXT CLEANING AND ANALYSIS
# ============================================================================

print("=== PRACTICE 2: TEXT CLEANING ===\n")

text = "Hello, World! This is Python."

# Convert to lowercase and remove punctuation
cleaned = text.lower().replace(',', '').replace('!', '').replace('.', '')
print(f"Original: {text}")
print(f"Cleaned: {cleaned}")

# Split into words and analyze
words = cleaned.split()
print(f"Word count: {len(words)}")
print(f"Words: {words}")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: FILE PATH PARSING
# ============================================================================

print("=== PRACTICE 3: FILE PATH PARSING ===\n")

filepath = "/home/user/documents/report.pdf"

# Extract filename
filename = filepath.split('/')[-1]
print(f"Full path: {filepath}")
print(f"Filename: {filename}")

# Extract extension
extension = filename.split('.')[-1]
print(f"Extension: {extension}")

# Check file type
is_pdf = filename.endswith('.pdf')
is_document = filename.endswith(('.pdf', '.doc', '.docx', '.txt'))
print(f"Is PDF: {is_pdf}")
print(f"Is Document: {is_document}")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: PASSWORD VALIDATION
# ============================================================================

print("=== PRACTICE 4: PASSWORD VALIDATION ===\n")

passwords = ["Pass123", "pass123", "12345", ""]

for pwd in passwords:
    # Check password strength
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    is_long = len(pwd) >= 8
    
    is_strong = has_upper and has_lower and has_digit and is_long
    
    print(f"Password: '{pwd}'")
    print(f"  Length >= 8: {is_long}")
    print(f"  Has uppercase: {has_upper}")
    print(f"  Has lowercase: {has_lower}")
    print(f"  Has digit: {has_digit}")
    print(f"  Is strong: {is_strong}\n")


# ============================================================================
# PRACTICE EXAMPLE 5: URL PARAMETER EXTRACTION
# ============================================================================

print("=== PRACTICE 5: URL PARSING ===\n")

url = "https://www.example.com/path/to/page?id=123&name=john&role=admin"

# Extract domain
domain = url.split('/')[2]  # Gets www.example.com
print(f"Full URL: {url}")
print(f"Domain: {domain}")

# Extract path
path = url.split('?')[0]
print(f"Path: {path}")

# Extract query string
if '?' in url:
    query_string = url.split('?')[1]
    print(f"Query: {query_string}")
    
    # Parse parameters
    params = query_string.split('&')
    print(f"Parameters:")
    for param in params:
        key, value = param.split('=')
        print(f"  {key}: {value}")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: NAME FORMATTING
# ============================================================================

print("=== PRACTICE 6: NAME FORMATTING ===\n")

names = ["john doe", "JANE SMITH", "bOb jOhNsOn"]

for name in names:
    # Proper case (title case)
    proper_name = name.title()
    
    # Extract initials
    parts = name.lower().split()
    initials = ''.join(p[0].upper() for p in parts)
    
    print(f"Raw: {name}")
    print(f"Proper: {proper_name}")
    print(f"Initials: {initials}\n")


# ============================================================================
# QUICK CHALLENGES
# ============================================================================

print("=== CHALLENGES ===")
print("1) Given 'hello world', capitalize each word.")
word = "hello world"
print(f" Capilized text : {word.capitalize()}")

print("2) Extract the domain from an email address (text before @).")
email = "jamesbanda@example.com"
print(f"Domain extracted from {email} is: {email.split('@')[0]}")

print("3) Count vowels (a, e, i, o, u) in a sentence.")
sentence = "This is an example sentence."
print(f"Number of vowels in '{sentence}': {sum(1 for c in sentence.lower() if c in 'aeiou')}")

print("4) Replace all vowels with asterisks in a word.")
word = "example"
print(f"Original: {word}")
print(f"Modified: {''.join('*' if c.lower() in 'aeiou' else c for c in word)}")

print("5) Check if a string is a palindrome (reads same forwards/backwards).")
print("\nTry implementing these!\n")

print("=== END OF STRING METHODS EXAMPLES ===")
