import re

def password_complexity_checker(password):
    # Define the criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_criteria = re.search(r'[\W_]', password)  # \W matches any non-word character

    # Count how many criteria are met
    criteria_met = sum([length_criteria, bool(uppercase_criteria), bool(lowercase_criteria), bool(number_criteria), bool(special_criteria)])

    # Determine strength based on number of criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")

    return {
        "password": password,
        "strength": strength,
        "feedback": feedback
    }

# Example usage:
if __name__ == "__main__":
    password = input("Enter a password to check its complexity: ")
    result = password_complexity_checker(password)
    print(f"Password: {result['password']}")
    print(f"Strength: {result['strength']}")
    if result['feedback']:
        print("Feedback:")
        for item in result['feedback']:
            print(f"- {item}")