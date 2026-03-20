# 📊 Open Economy Models Simulator (PyQt6)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Type](https://img.shields.io/badge/Type-Economic%20Simulation-green)
![Status](https://img.shields.io/badge/status-learning%20project-lightgreen)
![University](https://img.shields.io/badge/University-Warsaw-orange)

This project provides an interactive visualization of key macroeconomic models in an open economy framework.

Using a desktop application built with PyQt6 and Matplotlib, users can explore how changes in economic parameters affect equilibrium outcomes in real time.

---

## 📌 Current Model

### Small Open Economy *(Mała gospodarka otwarta)*

The application currently implements a simplified small open economy model, allowing users to analyze:

- Savings (S)
- Investment (I)
- World interest rate (r*)
- Capital flows (CF)
- Current account (CA)
- Real exchange rate (q)

### Key Features:

- Interactive sliders for all main parameters
- Real-time graph updates
- Visualization of:
  - Investment function I(r)
  - Savings (S)
  - Capital flows (CF)
  - Current account function CA(q)
- Automatic calculation of equilibrium:
  - Current account balance
  - Real exchange rate (q*)

---

## 📊 Example Visualizations

The application generates two main interactive plots:

1. **Loanable Funds Market**
   - Shows equilibrium between savings and investment
   - Determines capital flows (CF)

2. **Foreign Exchange Market**
   - Shows relationship between CA and real exchange rate (q)
   - Determines equilibrium exchange rate (q*)

---

## 🛠 Technologies

- Python
- PyQt6
- Matplotlib
- NumPy

---

## 📁 Project Structure
open-economy-models

│

├── main.py

├── ui/

│ ├── MainWindow.ui

│ ├── Classic.ui

│ └── ...

├── requirements.txt

└── README.md

---

## 🚧 Future Development

This project is actively being developed. Planned extensions include:

- Large Open Economy *(Duża gospodarka otwarta)*
- Interest Rate Parity *(Parytet stóp procentowych)*
- Mundell–Fleming Model
- Additional macroeconomic simulations
- Improved UI/UX and model switching

---

## 🎯 Purpose

The goal of this project is to:

- strengthen understanding of macroeconomic theory  
- build interactive economic simulations  
- develop practical programming skills in Python  
- create a portfolio-ready project for internships and junior roles  

---

## 👨‍💻 Author

**Arseniy Vanitskiy**  
University of Warsaw  
Economics & Mathematics

---

## 📌 Status

🚧 Work in Progress — new models and features will be added continuously.