import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Example usage
print(is_valid_email("user@domain.com"))  # True
print(is_valid_email("user@domain"))      # False
print(is_valid_email("user.name@site.co"))# True
print(is_valid_email("user@.com"))        # False
