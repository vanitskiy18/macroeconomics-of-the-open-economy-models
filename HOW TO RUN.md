# ▶️ HOW TO RUN

This guide explains how to run the **Open Economy Models Simulator** step by step, even if you have never launched a Python desktop application before.

---

## 1. What you need

To run this project, you need:

- **Python**
- required Python libraries:
  - `PyQt6`
  - `matplotlib`
  - `numpy`
- the project files in the correct folder structure

### Important:
You **do not need Qt Designer to run the app**.  
Qt Designer is only needed if you want to edit `.ui` interface files.

---

## 2. Install Python

If Python is not installed on your computer:

1. Go to the official Python website.
2. Download the newest stable Python 3 version.
3. Run the installer.
4. During installation, make sure to check:

Add Python to PATH

5. Finish the installation.

### How to check if Python is installed

Open **Command Prompt (cmd)** or **PowerShell** and type:

python --version

If python is installed correctly, you should see something like:

Python 3.12.0

---

## 3. Install Python IDLE (Python Shell)

Usually, IDLE is installed together with Python automatically

How to open IDLE:

After installing Python:
1. Open the Windows Start menu
2. Search for: IDLE
3. Open IDLE (Python 3.x)

### Important:
You can ALSO run the project through:
1. Command Prompt
2. PowerShell
3. VS Code
4. PyCharm

---

## 4. Download or copy the project

Place the whole project in one folder on your computer

Example:
C:\Users\YourName\Documents\open-economy-models

---

## 5. Make sure the folder structure is correct

The project should keep the same structure as described below:

open-economy-models
│
├── main.py
├── ui/
│   ├── MainWindow.ui
│   ├── Classic.ui
│   ├── Bilans.ui
│   └── ...
├── assets/
│   ├── model.png
│   ├── Bilans.png
│   └── ...
├── README.md
└── HOW_TO_RUN.md

### Important:
Do not move main.py away from the ui folder
The .ui files must stay in the proper place, otherwise the application may not load correctly.

---

## 6. Install required libraries

### Open Command Prompt or Power Shell in the project folder.

### The easiest way:
1. Open the project folder in File Explorer
2. Click in the folder path bar
3. Type: cmd
4. Press Enter
A terminal window will open directly in the project folder.

### Then install the libraries:
pip install PyQt6 matplotlib numpy

### If pip does not work
Try: python -m pip install PyQt6 matplotlib numpy
or: py -m pip install PyQt6 matplotlib numpy

---

## 7. Run the project

### Option A - run from IDLE
1. Open IDLE
2. CLick: File -> Open
3. Select main.py
4. In the opened editor window click:
Run -> Run Module
or press: F5
The application window should open.

### Option B - run from Command Prompt or Power Shell
If you are already in the project folder, type:
python main.py
If that does not work, try:
py main.py

---

## 8. What to do if something does not work

### Problem: No module named...
This means one of the required libraries is missing.

Install it with:
pip install PyQt6 matplotlib numpy

### Problem: application cannot find .ui files
This usually means the folder structure is incorrect

Make sure:
1. main.py is in the main project folder
2. .ui files are inside the ui/ folder
3. File names match exactly

### Problem: python command does not work
This usually means Python was not added to PATH.

Try: py main.py
if that works, Python is installed correctly.

### Problem: IDLE is missing
IDLE is usually installed with Python, but even ifi it is not available, the project can still be launched from:
python main.py

So IDLE is convenient, but not required
