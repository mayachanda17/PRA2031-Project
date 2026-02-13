# import pandas
print("Welcome to the budget planner!")
name = input("Please enter your name: ")
print("   ")
print("Hello", name)
print("   ")
age = int(input("Please enter your age: "))
height = int(input("Please enter your height (in centimeters): "))
budget = int(input("Please enter your budget: "))
"""print(age)
print(height)"""
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
gym_goer = input("Do you enjoy go to the gym? (Y/N)")
#if gym_goer.upper() == "Y":
    #call Budget child class
class Budget:
    def __init__(self, overall_budget):
        self.overall_budget = overall_budget 
        self.rent = overall_budget * .5
        self.food_budget = overall_budget * .1
        self.socialising_budget = overall_budget * .1
        self.exercising_budget = overall_budget * .1
        self.transportation_budget = overall_budget * .1
        self.emergency_fund = overall_budget * .1
    
class Gym(Budget): #creating a child class (inheritance) for someone who goes to the gym 
    def __init__ (self, overall_budget):
        super().__init__(overall_budget)
        self.exercise_budget_modifier = exercise_budget * 1.5

budget1 = Budget(budget) 
print("Your Rent Budget is €", budget1.rent)
print("Your Food Budget is €", budget1.food_budget)
print("Your Socialising Budget is €", budget1.socialising_budget)
print("Your Exercising Budget is €", budget1.exercising_budget)
print("Your Transportation Budget is €", budget1.transportation_budget)
print(budget1.emergency_fund, "€ is being added into your emergency fund")