import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_criteria = re.search(r"[@$!%*?&#]", password) is not None
    
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])
    
    strength = "Weak"
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character (@, $, !, %, *, ?, &, or #).")
    
    return strength, feedback

if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password strength: {strength}")
    for comment in feedback:
        print(f"- {comment}")
