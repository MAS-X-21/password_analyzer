# 🔐 Password Strength Analyzer & Security Suggestion Tool

> **A defensive cybersecurity application for evaluating password strength, detecting predictable patterns, and providing actionable security recommendations.**

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)
![Security](https://img.shields.io/badge/Focus-Defensive%20Security-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview

The **Password Strength Analyzer & Security Suggestion Tool** is a defensive cybersecurity project developed to demonstrate practical concepts in:

* Password security
* Secure coding
* Application security
* Identity & Access Management (IAM)
* Security awareness
* Pattern analysis
* Privacy-by-design

The application analyzes passwords **locally** and provides a security assessment based on multiple characteristics rather than relying only on traditional character-composition rules.

A password containing uppercase letters, lowercase letters, numbers, and symbols is **not automatically secure**.

For example:

```text
Password123!
```

may satisfy basic composition requirements while still being highly predictable.

This project therefore focuses on:

```text
LENGTH
    +
UNPREDICTABILITY
    +
PATTERN RESISTANCE
    +
COMMON-PASSWORD CHECKS
    +
CONTEXT AWARENESS
    =
BETTER PASSWORD ASSESSMENT
```

---

## 🎯 Objectives

The primary objectives of this project are to:

1. Analyze password strength locally.
2. Detect common and predictable passwords.
3. Identify repeated-character patterns.
4. Detect sequential patterns.
5. Detect common keyboard patterns.
6. Identify common dictionary terms.
7. Detect optional personal-context overlap.
8. Provide an entropy-style estimate.
9. Generate personalized security recommendations.
10. Promote secure password and passphrase practices.
11. Demonstrate privacy-preserving application design.
12. Provide an industry-oriented cybersecurity portfolio project.

---

# 🚀 Key Features

## 🔢 Password Strength Score

The application generates a security score from:

```text
0 – 100
```

with classifications:

| Score Range | Classification |
| ----------- | -------------- |
| 0–24        | 🔴 VERY WEAK   |
| 25–44       | 🟠 WEAK        |
| 45–64       | 🟡 MODERATE    |
| 65–84       | 🟢 STRONG      |
| 85–100      | 🟢 VERY STRONG |

The score considers multiple factors rather than relying solely on character composition.

---

## 📏 Length Analysis

Password length is one of the most important factors considered by the analyzer.

The application evaluates:

* Total password length
* Longer-password bonuses
* Unique character count
* Character diversity

Longer passwords and passphrases can provide significantly more search space than short passwords.

---

## 🔤 Character Diversity Analysis

The analyzer checks whether the password contains:

* Lowercase characters
* Uppercase characters
* Numbers
* Symbols
* Spaces

However, character diversity is treated as **one factor among several**, rather than the complete definition of password strength.

---

## 🚨 Common Password Detection

The application checks the password against a local demonstration list of common passwords.

Examples of predictable passwords include:

```text
password
password123
123456
qwerty
admin123
welcome
```

If an exact match is detected, the application generates a security warning.

> The included dataset is intentionally small and suitable for demonstration/testing. It should not be treated as a comprehensive breach corpus.

---

## 🔁 Repeated Character Detection

The analyzer detects patterns such as:

```text
aaa
111
!!!
aaaa
```

Repeated characters can reduce unpredictability and make passwords easier to guess.

---

## 🔢 Sequential Pattern Detection

The system detects predictable sequences such as:

```text
123
234
abc
xyz
```

and similar ascending or descending patterns.

---

## ⌨️ Keyboard Pattern Detection

Common keyboard sequences are analyzed, including patterns similar to:

```text
qwerty
asdf
zxcv
```

Keyboard walks are a common password weakness because they are easy for users to remember and attackers to model.

---

## 📖 Dictionary / Common-Word Detection

The application checks whether passwords contain common words or terms.

Examples:

```text
football
cricket
computer
student
welcome
password
```

This helps identify passwords constructed from predictable words.

---

## 👤 Personal Context Analysis

The application optionally accepts user-provided context such as:

```text
Username
Nickname
City
Organization
Other non-sensitive demo context
```

It then checks for overlap between the context and the password.

For example:

```text
Context:
Kozhikode Student

Password:
Kozhikode2026!
```

may generate a warning because the password contains information supplied as context.

> For demonstrations, use synthetic or non-sensitive information. Never enter sensitive personal information into screenshots or public demonstrations.

---

# 🧮 Entropy-Style Estimate

The application provides an **entropy-style estimate** measured in bits.

A simplified model is based on:

```text
H ≈ L × log₂(N)
```

where:

* `L` = password length
* `N` = estimated character pool size

For example, a password using lowercase, uppercase, digits, and symbols has a larger theoretical character pool.

### ⚠️ Important Limitation

This value is **not a guarantee of password security**.

Real-world password guessability can be significantly affected by:

* Human behavior
* Common password lists
* Dictionary attacks
* Personal information
* Keyboard patterns
* Password reuse
* Previously leaked credentials
* Attacker-specific guessing models

Therefore, this project treats entropy as an **educational estimate**, not a definitive security measurement.

---

# 🧠 Security Recommendation Engine

Based on detected weaknesses, the application generates actionable recommendations.

Examples include:

* Increase password length.
* Avoid common passwords.
* Avoid predictable sequences.
* Avoid keyboard patterns.
* Avoid personal information.
* Use unique passwords.
* Prefer long passphrases.
* Use a password manager.
* Enable Multi-Factor Authentication (MFA).

---

# 🛡️ Privacy & Security Design

Privacy is a core design principle of this project.

### The application does NOT:

❌ Store plaintext passwords
❌ Log passwords
❌ Upload passwords to external services
❌ Send passwords to APIs by default
❌ Implement password cracking
❌ Implement credential theft
❌ Collect user credentials

### Local Analysis

Password analysis is performed locally within the application.

```text
User
  │
  ▼
Password Input
  │
  ▼
Local Analysis Engine
  │
  ├── Length Analysis
  ├── Pattern Detection
  ├── Common Password Check
  ├── Dictionary Check
  ├── Context Analysis
  └── Entropy Estimate
  │
  ▼
Security Assessment
```

---

# 📊 Safe Local History

The application can optionally maintain local analysis history.

However, the history contains only **aggregate metadata**, such as:

```text
Timestamp
Score
Classification
Password Length
Unique Character Count
Warning Count
```

The actual password is **never stored**.

This demonstrates the principle:

> **Do not retain sensitive secrets when they are not required.**

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────┬───────────┘
                               │
                               ▼
                 ┌────────────────────────────┐
                 │ Password Analysis Engine   │
                 └─────────────┬──────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │          │           │           │           │
        ▼          ▼           ▼           ▼           ▼
     Length    Diversity    Patterns    Common     Context
     Analysis   Analysis    Detection   Password   Analysis
                                             │
                                             ▼
                                    ┌────────────────┐
                                    │ Entropy-Style  │
                                    │   Estimate     │
                                    └───────┬────────┘
                                            │
                                            ▼
                                  ┌──────────────────┐
                                  │ Scoring Engine   │
                                  └────────┬─────────┘
                                           │
                                           ▼
                                ┌─────────────────────┐
                                │ Security Suggestions│
                                └─────────────────────┘
```

---

# 📁 Project Structure

```text
password_strength_analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── password_analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── patterns.py
│   ├── scoring.py
│   ├── recommendations.py
│   └── history.py
│
├── data/
│   ├── common_passwords.txt
│   └── common_words.txt
│
├── screenshots/
│   ├── screenshot (77).png
│   ├── screenshot (78).png
│   └── screenshot (79).png
│
├── tests/
│   └── test_analyzer.py
│
└── docs/
    ├── PROJECT_REPORT.md
    ├── INTERVIEW_PREP.md
    └── SCREENSHOT_GUIDE.md
```

---

# 🖥️ Application Screenshots

The following screenshots demonstrate the application interface and its defensive password-analysis functionality.

### Screenshot 1 — Password Analysis Dashboard

![Password Analyzer Dashboard](screenshots/screenshot%20%2877%29.png)

---

### Screenshot 2 — Security Analysis & Recommendations

![Password Analyzer Analysis](screenshots/screenshot%20%2878%29.png)

---

### Screenshot 3 — Password Security Assessment

![Password Analyzer Result](screenshots/screenshot%20%2879%29.png)

> **Note:** Screenshots should contain synthetic/demo passwords only. Do not upload real passwords or sensitive information to GitHub.

---

# 🧪 Testing

Automated unit tests are included for important components of the application.

Testing covers:

* Empty password handling
* Common-password detection
* Sequence detection
* Keyboard-pattern detection
* Personal-context overlap
* Relative strength scoring

Run:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
OK
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/password-strength-analyzer.git
```

```bash
cd password-strength-analyzer
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🧰 Technologies Used

| Technology          | Purpose                              |
| ------------------- | ------------------------------------ |
| Python              | Core application logic               |
| Streamlit           | Interactive security dashboard       |
| SQLite              | Safe aggregate local history         |
| Regular Expressions | Pattern detection                    |
| UnitTest            | Automated testing                    |
| Git                 | Version control                      |
| GitHub              | Source-code management and portfolio |
| Markdown            | Documentation                        |

---

# 🔐 Cybersecurity Concepts Demonstrated

This project demonstrates practical knowledge of:

* Password Security
* Authentication Security
* Identity & Access Management
* Secure Coding
* Privacy by Design
* Input Analysis
* Pattern Recognition
* Security Awareness
* Defensive Application Security
* Data Minimization
* Local Data Processing
* Security Testing
* Risk-Based Recommendations

---

# ⚠️ Limitations

This project is an educational cybersecurity tool and should not be treated as a production-grade password-strength certification system.

Limitations include:

1. The common-password dataset is intentionally limited.
2. The dictionary dataset is intentionally limited.
3. Keyboard detection focuses on common QWERTY patterns.
4. Entropy is an educational estimate.
5. Human password behavior cannot be perfectly modeled with a simple score.
6. The score does not guarantee resistance against a specific attacker.

---

# 🔮 Future Enhancements

Potential improvements include:

* Larger vetted common-password datasets
* More keyboard layouts
* Advanced passphrase analysis
* Organization-specific password policies
* Improved password guessability modeling
* More sophisticated pattern detection
* Multilingual dictionary support
* Accessibility improvements
* Security policy configuration
* Additional automated tests
* Containerized deployment
* CI/CD security testing

---

# 🎓 Educational Value

This project was designed as a cybersecurity learning project to bridge theoretical security concepts with practical implementation.

It demonstrates how a security application can:

```text
Identify Risk
      ↓
Analyze Weakness
      ↓
Calculate Risk Indicators
      ↓
Explain the Finding
      ↓
Recommend Security Improvements
```

---

# 🧑‍💻 Author

**Muhammed Shammas**

B.Tech Computer Science Engineering
Cybersecurity / Software Development Enthusiast

### Areas of Interest

* Cybersecurity
* Application Security
* Secure Coding
* Python
* Identity & Access Management
* Security Automation
* Defensive Security

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⚖️ Ethical Disclaimer

This project is intended strictly for:

* Education
* Cybersecurity awareness
* Defensive security
* Secure software development
* Authorized testing

It does not provide password-cracking functionality, credential-stealing functionality, or unauthorized access capabilities.

**Never test passwords or credentials that you do not own or have explicit authorization to assess.**

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub and sharing it as part of your cybersecurity learning portfolio.

**Built for learning. Designed with security and privacy in mind.**
