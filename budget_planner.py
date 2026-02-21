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


class student: 
    """ this class focuss on academic buget """
    def __init__(self, device_cost=0, stationary_cost=0, printing_price=0, monthly_tuition_payment=0):
        self.device_cost = device_cost
        self.stationary_cost = stationary_cost
        self.printing_price = printing_price
        self.monthly_tuition_payment = monthly_tuition_payment
    """self at the begining is to store the info to the specific student"""
    """the =0 with each argument means that if the student doesnt put any values when the function is called then use 0 as a default """
    """this is good especially if somhow they are not the ones paying their monthly tuiton or if they dont use stationary cost(etc..)"""
    
    def what_do_you_use_to_study(self):
        print("\n what do you use to study?")
        print("1. only notebooks")
        print("2. only computers")
        print("3. only ipad")
        print("4. notebooks+ipad")
        print("5. notebooks+ computer")
        print("6. ipad+computer")

        choice =input("choose between (1-6): ")

        if choice == "1":
            self.stationary_cost = float(input( "Enter stationary cost: " ))
        
        elif choice == "2":
            owns_the_device = input("do you want include the cost of the device in your monthly spending ? (Y/N): ")
            if owns_the_device.upper() == "Y":
                cost= float(input("how much does it cost: "))
                monthly_spreading= int(input("how many month would you want to spread this cost over"))
                self.device_cost = cost / monthly_spreading
            else:
                self.device_cost = 0 

        elif choice == "3":
            owns_the_device = input("do you want include the cost of the device in your monthly spending ? (Y/N): ")
            if owns_the_device.upper() == "Y":
                cost = float(input("how much does it cost: "))
                monthly_spreading= int(input("how many month would you want to spread this cost over"))
                self.device_cost = cost / monthly_spreading
            else:
                self.device_cost = 0 

        elif choice == "4":
            owns_the_device = input("do you want include the cost of the device in your monthly spending ? (Y/N): ")
            if owns_the_device.upper() == "Y":
                cost = float(input("how much does it cost: "))
                monthly_spreading= int(input("how many month would you want to spread this cost over"))
                self.device_cost = cost / monthly_spreading
            else:
                self.device_cost = 0 
            self.stationary_cost = float(input( "Enter stationary cost: "))
        elif choice == "5":
            owns_the_device = input("do you want include the cost of the device in your monthly spending ? (Y/N): ")
            if owns_the_device.upper() == "Y":
                cost = float(input("how much does it cost: "))
                monthly_spreading= int(input("how many month would you want to spread this cost over"))
                self.device_cost = cost / monthly_spreading
            else:
                self.device_cost = 0     
            self.stationary_cost= float(input( "Enter stationary cost: "))
       
        elif choice == "6":
            owns_the_device = input("do you want include the cost of the device in your monthly spending ? (Y/N): ")
            if owns_the_device.upper() == "Y":
                cost = float(input("how much does it cost: "))
                monthly_spreading= int(input("how many month would you want to spread this cost over"))
                self.device_cost = cost / monthly_spreading
            else:
                self.device_cost = 0  
            self.stationary_cost = float(input( "Enter stationary cost: "))
  
    """\n makes a space in between the title and the questions making the structure cleaner"""
    """input function pauses the program and waits for the user to type smth on. whatever is in this argument will be stored in the variable "choice" """
    """float function takes the input let it be a bool( true becomes 1) a string (like "3.14" becomes 3.14) or an int ( 5 becomes 5.0) and converts the output into a float """

    def printing_usage (self): 
        printing= input("\n have you used the printing machine this month? (Y/N): ")
        if printing.upper() == "Y":
            pages = int(input("how many pages did you print"))
            colors_of_page= input("were the pages Black and white or Coloured? type (B/C) ")
            if colors_of_page.upper() == "B":
                price_per_page= 0.05
            else: 
                price_per_page= 0.15
            self.printing_price = pages * price_per_page 
        else: 
            self.printing_price = 0
    """ source: https://www.maastrichtuniversity.nl/upgrade-print-credit-students#:~:text=Attention:,remain%20unchanged%20at%2015%20cents."""
        
    def tuiton_fee (self):
        monthly_tuition= input("\n do you pay yourself a monthly tuiton (Y/N): ")
        if monthly_tuition.upper()== "Y":
            self.monthly_tuiton_payment= float(input("what is your monthly university payment?: "))
        else:
            self.monthly_tuition_payment= 0
    def total_monthly_academic_costs (self):
        total_monthly_academic_costs= (self.device_cost+self.stationary_cost +self.printing_price +self.monthly_tuition_payment)
        return total_monthly_academic_costs

"""note of print vs return: print prints whats inside fonction return sends the value out """
"""ngl i still dont fully get the concept of (self) and self."""

budget1 = Budget(budget) 
print("Your Rent Budget is €", budget1.rent)
print("Your Food Budget is €", budget1.food_budget)
print("Your Socialising Budget is €", budget1.socialising_budget)
print("Your Exercising Budget is €", budget1.exercising_budget)
print("Your Transportation Budget is €", budget1.transportation_budget)
print(budget1.emergency_fund, "€ is being added into your emergency fund")
