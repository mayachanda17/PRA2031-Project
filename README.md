# Student Budget Planner

Student Budget Planner is a Python project that helps students estimate and organize their monthly expenses in Maastricht. It combines personal health calculations, budgeting logic, student-related academic costs, and visualisations in one command-line application.

---

## Description

The program collects personal and financial information from the user and then calculates:

- Personal health metrics such as **BMI**, **BMR**, and estimated **daily calorie needs**
- An estimated **grocery budget** based on calorie needs
- Monthly expense priorities such as **rent, groceries, insurance, subscriptions, gifts, debts, and savings**
- Academic costs such as **tuition, printing, stationery, and device-related costs**
- Visual summaries of budget data

The project is built using **Object-Oriented Programming (OOP)**, with separate classes handling personal information, budgeting, priorities, and student expenses.

This program is intended as a guideline to help organise and estimate student expenses. It should not be used as a definitive or precise budget calculation tool.

---

## Features

- Monthly budget breakdown
- Expense priority analysis
- Student academic cost calculator
- Personalised grocery budget estimate
- Health-related calculations (BMI, BMR, calorie needs)
- Data visualisation using `matplotlib`

---

## Project Structure

```
PRA2031-Project/
│
├── src/
│   ├── budget_planner.py       # Main program file
│   ├── class_budget.py         # Budget calculations
│   ├── class_person.py         # Personal health calculations
│   ├── class_priorities.py     # Priority and spending logic
│   ├── class_student.py        # Academic expense calculations
│   ├── visualisation.py        # Graphs and plots
│   └── average_costs.txt       # Supporting cost data
│
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## Classes Overview

### Person
Handles personal health-related calculations, including:

- BMI
- BMR
- Activity level
- Daily calorie needs
- Estimated grocery budget

### Budget
Handles financial calculations such as:

- Total expenses
- Remaining budget
- Monthly budget breakdown

### Priorities
Manages how income is distributed across spending categories such as:

- Rent
- Groceries
- Insurance
- Bike subscription
- Gym subscription
- Going out
- Hair salon
- Hygienic products
- Gifts
- Debts
- Savings

### Student
Calculates monthly academic expenses, including:

- Tuition
- Printing
- Stationery
- Study device costs

### Visualisation
Creates graphs for:

- Budget distribution
- Expense priorities
- Calorie-related data

---

## Requirements

- Python **3.8 or higher**
- `pip`
- `matplotlib`

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mayachanda17/PRA2031-Project.git
cd PRA2031-Project
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the program with:

```bash
python src/budget_planner.py
```

---

## Example Interaction

```
Welcome to the budget planner!

Please enter your name: John
Please enter your age: 20
Enter whether you are a MAN or WOMAN: MAN
Please enter your height (in centimeters): 175
Please enter your weight (in kilos): 70
Enter your activity level (1-5): 3
Please enter your monthly budget: 1000
```

The program then calculates:

- Personal health results
- Budget breakdown
- Expense priorities
- Academic costs
- Visualisations

---

## Libraries Used

- Python standard library
- `math`
- `matplotlib`

---

## Future Improvements

- Add file export for results
- Improve error handling and input validation
- Add more detailed spending categories
- Add a graphical user interface
- Support saving and comparing multiple student profiles

---

## Authors

- Maya Chanda — ma.chanda@student.maastrichtuniversity.nl  
- Szonja Szekeres — s.szekeres@student.maastrichtuniversity.nl  
- Szymon Stembalski — s.stembalski@student.maastrichtuniversity.nl  
- Maya Eden — m.gohy@student.maastrichtuniversity.nl  
- Mila Croci — m.croci@student.maastrichtuniversity.nl  

---

## AI Assistance Disclosure

AI tools (ChatGPT) were used during the development of this project to assist with debugging, code explanations, and documentation improvements. The authors reviewed, modified, and verified all suggested code to ensure correctness and understanding. All final design decisions and implementation were made by the project authors.

---

## License

Academic project — not for commercial use.
