def is_strong_password(password):

 # Check the length of the password
 if len(password) < 8:
   return False

 # Check for uppercase letters
 has_uppercase = False
 for char in password:
   if char.isupper():
     has_uppercase = True
     break

 # Check for lowercase letters
 has_lowercase = False
 for char in password:
   if char.islower():
     has_lowercase = True
     break

 # Check for digits
 has_digit = False
 for char in password:
   if char.isdigit():
     has_digit = True
     break

 # Check for special characters
 has_special = False
 for char in password:
   if char in "#?!$":
     has_special = True
     break

 # Return True if all the conditions are met
 if(not has_uppercase or not has_lowercase or not has_digit or not has_special):
   return "Weak password"
 else:
   return "Strong password"

    