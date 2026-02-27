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
    def __init__(self, name, age, height, gender, bmi, activity_level, bmr, calorie_needs):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.bmi = bmi
        self.activity_level = activity_level
        self.bmr = bmr
        self.calorie_needs = calorie_needs

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    @property
    def height(self):
        return self._height
    @height.setter
    def height (self,height):
        if height < 0 and height > 272:
            raise ValueError("Height cannot be negative or greater than 272 cm")
        self._height=height

    @property
    def gender(self):
        gender input ("Write either "Born as a man" or "Born as a woman":")
    @gender.setter
    def gender(self,gender):
        if gender =/ "born as a man" and gender =/ "born as a wmoman":
            raise ValueError("Gender not defined")
        self._gender=gender

    @property
    def bmi(self):
        return weight / ((height/100) ** 2)
    @bmi.setter
    def bmi(self, bmi):
        if bmi < 18.5:
            print ("You are underweight")
        elif bmi < 25:
            print ("You are normal weight")
        elif bmi < 30:
            print ("You are overweight")
        else:   
            print ("You are overweight")
        self._bmi=bmi

    @property
    def activity_level (self):
        activity_level = input("How active are you? (1-5, 1 being not active at all and 5 being very active):")
        if activity_level == "1":
            return "sedentary"
        if activity_level == "2":
            return 'light activity level'
        if activity_level == "3":
            return "moderate activity level"
        if activity_level == "4":
            return "high activity level"
        if activity_level == "5":
            return "athlete "
    @activity_level.setter
    def activity_level(self,activity_level):
        if level <1 or level >5:
            raise ValueError("Activity level must be between 1 and 5")
        self._activity_level = activity_level  

    @property
    def bmr (self):
        self._bmr
    @bmr.setter
    def bmr(self, bmr):
        if self._gender == "Born as a man":
            bmr: 10 * weight + 6.25 * height - 5 * age + 5
        else :
            bmr: 10 * weight + 6.25 * height - 5*age -161
        self._bmr= bmr

    @property
    def calorie_needs(self):
        #Step 1: Multiply BMR by activity level factor
        if self._activity_level == "sedentary":
            calorie_needs = self._bmr + 1.2
            elif self._activity_level == "light activity level":
            calorie_needs = self.bmr * 1.375
        elif self.activity_level == "moderate activity level":
            calorie_needs = self._bmr * 1.55
        elif self._activity level == "high activity level":
            calorie_needs = self._bmr * 1.725
        elif self._activity_level == "athlete":
            calorie_needs = sefl._bmr * 1.9
        self._calorie_needs = calorie_needs
        #Step 2 = Adjust for age ( depending on metabolism slowing down with age)
        if self.age < 18: 
            calories *= 1.15 # growing teens need 15% more calories
        elif self.age > 25:
            calories *= 1.10 # need 10% more
        elif self.age < 30:
            calories *= 1.05 # need 5% more
            elif self.age < 40:
            pass # as is
        elif self.age < 50:
            calories *= 0.97 # slows down 3%
        elif self.age < 60:
            calories *= 0.94 # slows down 6%
        elif self.age < 70:
            calories *= 0.91 # slows doxn 9%
        else:
            calories = 0.88
        #Step 3 = adjust for bmi
        if self.bmi < 18.5:
            calories += 300
        elif self.bmi < 25:
            pass
        elif self.bmi < 30:
            calories -= 300
        else:
            calories -= 500
        return round(calories)

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

class Priorities :

    def __init__(self, rent, groceries, insurance, bike_subscription, gym_subscription, going_out, hair_salon, hygenic_products, gifts, debts, savings):
     self.rent = rent
     self.groceries = groceries 
     self.insurance = insurance
     self.bike_subscription = bike_subscription
     self.gym_subscription = gym_subscription
     self.going_out = going_out
     self.hair_salon = hair_salon
     self.hygenic_products = hygenic_products
     self.gifts = gifts
     self.debts = debts
     self.savings = savings

    def priority_of_activities(self):
       from flask import Flask, request, jsonify
       app = Flask(__Budget_calculator__) 
       activities = {  "rent" : price(),
        "groceries" : price()
        "insurance" : price(),
        "bike_subscription" : price(),
        "gym_subscription" : price(),
        "going_out" : price(),
        "hair_salon" : price (),
        'hygenic_produtcs': price(),
        "gitfs" : price(),
        "debts" : price(),
        "savings" : price() }
    def compute_priorities(activities):
        total = sum (activities.values())

        if total == 0:
            return  {k: 0 for k in activities}
        return  {k: v / total for k, v in activities.items()}
    
    @app.route('/priorities', methods=["POST"] )
    def calculate_priorities():
        data = request.get_json()
        priorities = compute_priorities(data)
        return jsonify(priorities)
    
    if __Budget_calculator__ == '__main__':
        app.run(debug=True)
        app.py
        
     print(priority_of_activities)

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
