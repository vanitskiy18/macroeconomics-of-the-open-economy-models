# 📊 Open Economy Models Simulator (PyQt6)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Type](https://img.shields.io/badge/Type-Economic%20Simulation-green)
![Status](https://img.shields.io/badge/status-learning%20project-lightgreen)
![University](https://img.shields.io/badge/University-Warsaw-orange)

This project provides an interactive visualization of key macroeconomic mechanisms in an open economy framework.

Using a desktop application built with **PyQt6** and **Matplotlib**, users can explore how changes in economic parameters affect equilibrium outcomes in real time.

---

## 📌 Current Model

### Classical Open Economy Model *(Model klasyczny gospodarki otwartej)*

The application currently implements a simplified graphical representation of the classical open economy model within a **unified interface**.

Instead of separating small and large open economy cases, the model combines key relationships into one consistent visualization environment.

Users can analyze interactions between:

- Savings (**S**)
- Investment and capital flows (**I(r) + CF(r)**)
- Exogenous interest rate (**r = r\***)
- Capital flows (**CF**)
- Current account (**CA**)
- Real exchange rate (**q**)

---

## 📊 Visualizations

The application generates two main interactive plots:

1. **Savings–Investment / Capital Flows Diagram**
   - illustrates the relationship between savings and the investment–capital flow schedule,
   - shows equilibrium at a given interest rate (**r = r\***),
   - determines the implied capital flows (**CF = S − I**).

2. **Current Account and Real Exchange Rate Diagram**
   - shows the relationship between the current account (**CA**) and real exchange rate (**q**),
   - determines equilibrium exchange rate (**q\***),
   - allows analysis of shifts in the current account function.

Both graphs are dynamically updated using sliders, enabling real-time comparative statics.

---

## 📸 Screenshots

### Classical Open Economy Model

![Model](./assets/model.png)

### Topic Selection Interface

![Menu](./assets/menu.png)

---

## ⚙️ Key Features

- Interactive sliders for all main parameters
- Real-time graph updates
- Unified model interface (no separate windows)
- Automatic equilibrium calculation
- Visualization of:
  - **S**
  - **I(r) + CF(r)**
  - **CF**
  - **CA(q)**
  - **r = r\***
  - **q**

---

## 📎 Model Notes

- The model is a simplified educational representation.
- Some parameter combinations may generate economically unrealistic values (e.g., negative *q*), which are intentionally allowed to preserve graphical clarity and flexibility.
- The identity **S − I = CF** is imposed within the model structure.

---

## 🛠 Technologies

- Python
- PyQt6
- Matplotlib
- NumPy

---

## 📁 Project Structure


## 📁 Project Structure
open-economy-models

│

├── main.py

├── ui/

│ ├── MainWindow.ui

│ ├── Classic.ui

│ └── ...

├── screenshots/

│ ├── ...

├── requirements.txt

└── README.md


---

## 🚧 Future Development

This project is actively being developed. Planned extensions include:

- **Intertemporal approach to the balance of payments**  
  *(podejście międzyokresowe do bilansu płatniczego)*
- Interest Rate Parity *(Parytet stóp procentowych)*
- Mundell–Fleming Model
- Additional macroeconomic simulations
- Improved UI/UX and model extensions

---

## 🎯 Purpose

The goal of this project is to:

- strengthen understanding of macroeconomic theory  
- build interactive economic simulations  
- develop practical programming skills in Python  
- create a high-quality project demonstrating the ability to combine economics and software development  

The project also serves as part of a personal portfolio for internships and entry-level roles in data analysis and finance.

---

## 👨‍💻 Author

**Arseniy Vanitskiy**  
University of Warsaw  
Economics & Mathematics  

---

## 📌 Status

🚧 Work in Progress — new models and features are continuously being added.