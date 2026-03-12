from visualisation import (
    plot_budget_distribution, 
    plot_priorities,
    plot_calorie_needs
)
from class_person import Person
from class_budget import Budget
import class_budget
#print(class_budget.__file__)
#print(Budget)
from class_priorities import Priorities
import class_priorities
print("Using file:", class_priorities.__file__)
from class_student import Student

print("Welcome to the budget planner!")
print()

# -------------------------
# PERSONAL INFORMATION
# -------------------------
name = input("Please enter your name: ")
print()
print("Hello", name)
print()

age = int(input("Please enter your age: "))
gender = input("Enter whether you are a MAN or WOMAN: ")
height = float(input("Please enter your height (in centimeters): "))
weight = float(input("Please enter your weight (in kilos): "))
activity_level = int(input("Enter your activity level (1-5): "))
budget = float(input("Please enter your monthly budget: "))

# -------------------------
# CREATE MAIN OBJECTS
# -------------------------
person1 = Person(name, age, height, weight, gender, activity_level)


# -------------------------
# PRIORITIES INPUT
# -------------------------
print()
print("--- MONTHLY EXPENSE PRIORITIES ---")
priorities1 = Priorities (
income = float(input("Enter your income:")),
rent = float(input("Enter your rent price: ")),
groceries = float(input("Enter your groceries price: ")),
insurance = float(input("Enter your insurance price: ")),
bike_subscription = float(input("Enter your bike subscription price: ")),
gym_subscription = float(input("Enter your gym subscription price: ")),
going_out = float(input("Enter your going out price: ")),
hair_salon = float(input("Enter your hair salon price: ")),
hygenic_products = float(input("Enter your hygienic products price: ")),
gifts = float(input("Enter your preferred gifts budget: ")),
debts = float(input("Enter your debts price: ")),
savings = float(input("Enter your preferred savings amount: ")),
)
budget1 = Budget(priorities1)
print(dir(budget1))
print("Total expenses:", budget1.total_expenses())
print("Remaining budget:", budget1.remaining_budget())

# -------------------------
# STUDENT INPUT
# -------------------------
print()
print("--- ACADEMIC COSTS ---")
student1 = Student()
student1.what_do_you_use_to_study()
student1.printing_usage()
student1.tuiton_fee()

# -------------------------
# PRINT RESULTS
# -------------------------
print()
print("========== PERSONAL HEALTH RESULTS ==========")
print("Name:", person1.name)
print("Age:", person1.age)
print("Height:", person1.height, "cm")
print("Weight:", person1.weight, "kg")
print("Gender:", person1.gender)
print("BMI:", round(person1.bmi, 2))
print(person1.bmi_category())
print("BMR:", round(person1.bmr, 2))
print("Estimated daily calorie needs:", person1.calorie_needs)
print("Estimated monthly grocery budget: €", person1.estimated_grocery_budget())

print()
print("========== BUDGET BREAKDOWN ==========")
for category, amount in budget1.monthly_priority_costs().items():
    print(f"{category}: €{amount}")

print()
print("========== EXPENSE PRIORITIES ==========")
activities = priorities1.priority_of_activities()
print("activities =", activities)
print("object type =", type(priorities1))

is_student= input("Are you a student? (yes/no):").strip().lower() 
if is_student:
    print("========== ACADEMIC COSTS ==========")
    print("Device cost per month: €", round(student1.device_cost, 2))
    print("Stationary cost: €", round(student1.stationary_cost, 2))
    print("Printing cost: €", round(student1.printing_price, 2))
    print("Monthly tuition payment: €", round(student1.monthly_tuition_payment, 2))
    print("Total monthly academic costs: €", round(student1.total_monthly_academic_costs(), 2))

# -------------------------
# VISUALISATIONS
# -------------------------
plot_budget_distribution(budget1)
activities = priorities1.priority_of_activities()
print("activities:", activities)
plot_priorities(activities)
plot_priorities(activities)
plot_calorie_needs(person1.bmr)
