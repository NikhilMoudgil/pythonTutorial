#Problem: Check if a password is "Weak", "Medium", or "Strong".
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
password = input("Enter your password: ")
if len(password) < 6:
    strength = "Weak"
    
elif 6 <= len(password) <= 10:
    strength = "Medium"
  
else:
    strength = "Strong"
    
print(f"Your password is {strength}..")