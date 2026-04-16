# 📊 Open Economy Models Simulator (PyQt6)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Type](https://img.shields.io/badge/Type-Economic%20Simulation-green)
![Status](https://img.shields.io/badge/status-learning%20project-lightgreen)
![University](https://img.shields.io/badge/University-Warsaw-orange)
![UI](https://img.shields.io/badge/UI-PyQt6-blueviolet)
![Rendering](https://img.shields.io/badge/HTML-Enabled-orange)

This project provides an interactive visualization of key macroeconomic mechanisms in an open economy framework, combining real-time simulation with theoretical economic models.

Using a desktop application built with **PyQt6**, **Matplotlib**, and embedded **HTML rendering**, users can explore how changes in economic parameters affect equilibrium outcomes in real time.

---

## 📌 Current Models

The application currently implements three core macroeconomic frameworks within a **unified interface**:

---

### 1. Classical Open Economy Model  
*(Model klasyczny gospodarki otwartej)*

A graphical representation of the standard open economy model, integrating key relationships into one consistent visualization environment.

Users can analyze interactions between:

- Savings (**S**)
- Investment and capital flows (**I(r) + CF(r)**)
- Exogenous interest rate (**r = r\***)
- Capital flows (**CF**)
- Current account (**CA**)
- Real exchange rate (**q**)

---

### 2. Intertemporal Approach to the Balance of Payments  
*(Podejście międzyokresowe do bilansu płatniczego)*

A dynamic two-period model illustrating intertemporal consumption choices and external balance.

The visualization includes:

- Budget constraint:
  - slope: **−(1 + r)**
- Intertemporal consumption:
  - **C₁, C₂**
- Endowment points:
  - **Y₁, Y₂**
- Utility maximization:
  - **U = C₁^β · C₂^(1−β)**
- Equilibrium point (**Eₐ**)
- Intertemporal trade interpretation

Additionally, the model features:

- Approximate **Production Possibility Frontiers (PPF)**  
  modeled as smooth curves attached to the budget line
- Comparative statics via:
  - interest rate (**r**)
  - time preference (**β**)

---

### 3. Interest Rate Parity (UIP)  
*(Parytet stóp procentowych)*

An interactive visualization of the uncovered interest rate parity condition, presented in two complementary variants:

#### • UIP (standalone)

A financial market perspective where the domestic interest rate is determined by the intersection of:

- Domestic return function: **RETᴰ(i)**
- Foreign return function: **RETᶠ(Eᵉ, i*, ρ)**

Users can analyze:

- expected exchange rate (**Eᵉ**)
- foreign interest rate (**i\***)
- risk premium (**ρ**)
- equilibrium determination of:
  - interest rate (**i**)
  - exchange rate (**E**)

---

#### • UIP + Money Market

An extended version integrating the UIP condition with the money market.

The model combines:

- Money supply: **M/P**
- Money demand: **L(Y, i)**
- Interest rate determination via money market equilibrium

This allows users to observe how:

- changes in **M/P** or **Y** affect **i**
- which in turn shifts equilibrium in the UIP framework
- monetary shocks transmit into exchange rate movements

---

## 📊 Visualizations

The application generates multiple interactive plots:

### Classical Model:
1. **Savings–Investment / Capital Flows Diagram**
   - relationship between savings and investment–capital flow schedule
   - equilibrium at **r = r\***
   - capital flows: **CF = S − I**

2. **Current Account and Real Exchange Rate Diagram**
   - **CA(q)** relationship
   - equilibrium exchange rate (**q\***)
   - shifts in current account

---

### Intertemporal Model:
3. **Intertemporal Consumption Diagram**
   - budget line and optimal consumption choice
   - utility curves
   - PPF (present / future orientation)
   - equilibrium adjustment

---

### UIP Models:
4. **Interest Rate Parity Diagram**
   - intersection of **RETᴰ(i)** and **RETᶠ(Eᵉ, i*, ρ)**
   - determination of equilibrium **i** and **E**
   - shifts driven by expectations and risk premium

5. **UIP with Money Market**
   - interaction between **money market (M/P, L(Y,i))** and UIP
   - indirect determination of exchange rate through **i**
   - transmission of monetary shocks to the exchange rate

---

## 📸 Screenshots

### Intertemporal Model

![Intertemporal](./screenshots/Bilans.jpg)

### Classical Model

![Model](./screenshots/open_economy.jpg)

### Interest Rate Parity

![UIP](./screenshots/par_int_rate_1.jpg)

### UIP + Money Market

![UIP+MM](./screenshots/par_int_rate.jpg)

### Topic Selection Interface

![Menu](./screenshots/main_window.jpg)

---

## ⚙️ Key Features

- Interactive sliders for key parameters:
  - interest rate (**r**)
  - time preference (**β**)
  - money supply (**M/P**)
  - expected exchange rate and financial parameters
- Real-time graph updates
- Automatic equilibrium calculation
- Multiple macroeconomic frameworks in one application
- Visualization of:
  - **S, I, CF**
  - **CA(q)**
  - **intertemporal consumption (C₁, C₂)**
  - **RETᴰ and RETᶠ functions**
  - **money market equilibrium**
- Dual-mode UIP analysis:
  - standalone financial market
  - integrated with money market

---

## 🧠 Model Notes

- The models are simplified educational representations.
- Some parameter combinations may generate economically unrealistic values (e.g., negative *q*), which are intentionally allowed for visualization purposes.
- The identity **S − I = CF** is imposed.
- In the intertemporal model, **PPF curves are approximated using parametric functions attached to the budget line**.
- In the UIP standalone model, the interest rate is determined by the intersection of **RETᴰ(i)** and **RETᶠ(Eᵉ, i*, ρ)**.
- In the extended UIP model, the interest rate is determined via the money market and transmitted to the exchange rate.
- Risk premium (**ρ**) is treated as an exogenous parameter reflecting financial market conditions.

---

## 🧾 UI & Rendering

- Graphs are rendered using **Matplotlib**
- Interface built with **PyQt6**
- Mathematical descriptions and model assumptions are displayed using **embedded HTML (QTextBrowser)**

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

│ ├── Bilans.ui

│ ├── par_int_rate.ui

│ └── ...

├── screenshots/

│ ├── ...

├── requirements.txt

├── HOW TO RUN.md

└── README.md

---

## 🚧 Future Development

This project is actively being developed. Planned extensions include:

- Mundell–Fleming Model
- Advanced UIP extensions (expectations formation, dynamics)
- Additional macroeconomic simulations
- Improved graphical accuracy of PPF curves
- UI/UX improvements

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