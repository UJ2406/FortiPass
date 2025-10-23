# 🔒 FortiPass

FortiPass is a modern Python-based password strength tester designed for security awareness and portfolio showcasing. It analyzes password strength using entropy calculations, OWASP guidelines, and pattern detection—all in a privacy-friendly way. No actual passwords are ever stored, only analysis metrics.

---

## 🎯 Overview

**FortiPass** helps users check the robustness of their passwords and learn best practices for secure authentication. It provides:

- Entropy measurement (in bits)
- OWASP-based feedback
- Detection of risky patterns & common passwords
- Actionable, clear guidance to improve your passwords
- Privacy-first logging

Perfect for students, cybersecurity professionals, developers, and anyone interested in boosting password hygiene!

---

## 🚀 Features

- 🟢 **Interactive menu-driven CLI interface**
- 🟢 **Entropy calculation:** grades password strength as Weak, Medium, or Strong
- 🟢 **OWASP-compliant feedback:** shows what’s missing for a stronger password
- 🟢 **Common pattern detection:** flags weak, popular choices
- 🟢 **Log summary:** view stats for all analyzed passwords (`length` and `entropy` only)
- 🟢 **Zero dependencies:** pure Python, no external packages needed
- 🟢 **No password storage:** only anonymized metrics logged

---

## 🛠️ Installation

1. **Clone the repository**
    ```
    git clone https://github.com/UJ2406/fortipass.git
    cd fortipass
    ```


2. **Run the tool**
    ```
    python password_tester.py
    ```

---

## 🎬 Usage

1. Start the script:
    ```
    python password_tester.py
    ```
2. Select menu options:
   - `1. Test a new password`
   - `2. View analysis log summary`
   - `3. Exit`

3. Sample session:
    ```
    ====== Password Strength Tester ======
    1. Test a new password
    2. View analysis log summary
    3. Exit
    Select an option (1-3): 1

    Enter password to analyze: FortiPass!2025

    Entropy: 87.58 bits
    Strength Evaluation:
    Strong (safe against brute-force)

    OWASP Feedback:
    - Good password! Meets OWASP guidelines.
    ```

---


## 💡 Learning Outcomes

- Understand password entropy and brute-force risks
- Apply OWASP password security recommendations
- Identify and avoid common insecure patterns
- Explore Python's regex and analysis techniques
- Build user-friendly CLI cybersecurity tools

---

## 🏷️ Topics & Tags

`python` `cybersecurity` `password-strength` `owasp` `entropy` `security-tool` `cli`

---

## 📚 References

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Password Entropy Calculation](https://en.wikipedia.org/wiki/Password_strength)

---

## 👏 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🙋 Frequently Asked Questions

**Q: Does FortiPass save my passwords?**  
*A: No. Only the analysis metrics (`length` and `entropy`) are logged for privacy.*

**Q: Is FortiPass cross-platform?**  
*A: Yes. It runs on Windows, Linux, and MacOS (Python 3.7+).*

**Q: Can I test multiple passwords in one run?**  
*A: Yes! Use the interactive menu to test as many as you like.*

---

## 📁 Repository Content

The repository contains the following files and folders:
```
FortiPass/
├── README.md              # This file – Complete documentation
├── password_tester.py     # Main menu-driven password strength tester
├── requirements.txt       # (Optional) Python requirements (uses only standard library)
├── screenshots             #  demo images

```
---


## 🔗 Connect

For issues, suggestions, or collaboration, please open a GitHub issue or reach out via email: ujjwalshield@example.com

---



