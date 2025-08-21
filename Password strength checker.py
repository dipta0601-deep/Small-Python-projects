import string

print("Enter a password with a criteria of (length, uppercase, digits, symbols).")

password = input("enter the password: ")

min_len = 8
has_lower = False
has_upper = False
has_symbol = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in string.punctuation:
        has_symbol = True

if len(password) < min_len:
    print("Weak Password")
elif not(has_lower, has_upper, has_digit, has_symbol):
    print("Moderate password")
else:
    print("strong password")