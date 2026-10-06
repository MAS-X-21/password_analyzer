# 🛡️ Password Strength Analyzer & Security Suggestion Tool

A robust, local-first defensive cybersecurity application built to evaluate password entropy, identify predictable patterns, and provide actionable security recommendations without storing, logging, or transmitting user credentials.

## 🚀 Features
- **Local Entropy Calculation:** Computes Shannon entropy (H = L * log2(R)) to gauge unpredictability.
- **Advanced Pattern Detection:** Identifies keyboard walks (`qwerty`), sequential runs (`123`), and repeated character loops.
- **Common Password Screening:** Flags passwords matching known breach datasets.
- **Contextual Awareness:** Allows users to test passwords against personal data strings (names, dates) to prevent social engineering weaknesses.
- **Interactive GUI Dashboard:** Built using Streamlit for clean data visualization.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Framework:** Streamlit
- **Testing:** Pytest

## ⚙️ Installation & Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-strength-analyzer.git
   cd password-strength-analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run app.py
   ```
