import matplotlib.pyplot as plt
"""Plot the visualisations"""
def plot_budget_distribution(budget):
    data = budget.monthly_priority_costs()

    labels = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Monthly Budget Distribution")
    plt.show()

def plot_priorities(priorities):
    names = list(priorities.keys())
    values = list(priorities.values())

    plt.figure()
    plt.bar(names, values)

    plt.xlabel("Expense Category")
    plt.ylabel("Cost (€)")
    plt.title("Priority of Expenses")

    plt.xticks(rotation=45)

    plt.show()

def plot_calorie_needs(bmr):
    activity_levels = [
        "Sedentary",
        "Light",
        "Moderate",
        "High",
        "Athlete"
    ]

    factors = [1.2, 1.375, 1.55, 1.725, 1.9]

    calories = [bmr * f for f in factors]

    plt.figure()

    plt.plot(activity_levels, calories, marker='o', label="Daily Calories")

    plt.xlabel("Activity Level")
    plt.ylabel("Calories Needed per Day")
    plt.title("Effect of Activity Level on Daily Calorie Needs")

    plt.legend()
    plt.grid(True)

    plt.show()
