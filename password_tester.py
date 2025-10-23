import re
import math
import os

def entropy(password):
    pool = 0
    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"\d", password):
        pool += 10
    if re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
        pool += 32
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 2)

def owasp_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password is too short. Minimum 8 characters recommended.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add uppercase letters for better strength.")
    if not re.search(r"[a-z]", password):
        feedback.append("Add lowercase letters for better strength.")
    if not re.search(r"\d", password):
        feedback.append("Add digits for better strength.")
    if not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
        feedback.append("Add special characters for better strength.")
    common_patterns = ['password', '123456', 'qwerty', 'letmein']
    for pattern in common_patterns:
        if pattern in password.lower():
            feedback.append(f"Don't use common words/pattern like '{pattern}'.")
    if not feedback:
        feedback.append("Good password! Meets OWASP guidelines.")
    return feedback

def print_log_summary():
    if not os.path.exists("tester.log"):
        print("\nNo analyses have been logged yet.")
        return
    print("\n== Log Summary ==")
    with open("tester.log", "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            print(f"{idx}. {line.strip()}")

def analyze_password():
    password = input("\nEnter password to analyze: ")
    bits_entropy = entropy(password)
    print(f"\nEntropy: {bits_entropy} bits")
    print("Strength Evaluation:")
    if bits_entropy < 28:
        print("Weak (easy to guess)")
    elif bits_entropy < 36:
        print("Medium (could be brute-forced)")
    else:
        print("Strong (safe against brute-force)")
    print("\nOWASP Feedback:")
    for f in owasp_feedback(password):
        print(f"- {f}")
    # Log result (not password itself)
    with open("tester.log", "a") as f:
        f.write(f"Length:{len(password)} Entropy:{bits_entropy}\n")

def main_menu():
    while True:
        print("\n====== Password Strength Tester ======")
        print("1. Test a new password")
        print("2. View analysis log summary")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            analyze_password()
        elif choice == '2':
            print_log_summary()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid selection. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()
