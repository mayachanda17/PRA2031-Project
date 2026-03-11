<<<<<<< HEAD
# import pandas
print("Welcome to the budget planner!")
name = input("Please enter your name: ")
print("   ")
print("Hello", name)
print("   ")
age = int(input("Please enter your age: "))
sex = input("Enter whether you are a MAN or WOMAN:")
sex = sex.upper()
height = int(input("Please enter your height (in centimeters): "))
weight = int(input("Please enter your weight (in kilos): "))
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
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, sex):
       if sex not in ["MAN", "WOMAN"]:
            raise ValueError("For this program, sex must be either a man or woman!")
       self._sex = sex

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
    def activity_level(self, activity_level):
        if activity_level <1 or activity_level >5:
            raise ValueError("Activity level must be between 1 and 5")
        self._activity_level = activity_level  

    @property
    def bmr(self):
        self._bmr
    @bmr.setter
    def bmr(self, bmr):
        if self._gender == "MAN":
            self._bmr = (10 * weight + 6.25 * height - 5 * age + 5)
        else :
            self._bmr = 10 * weight + 6.25 * height - 5*age -161
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
        elif self._activity_level == "high activity level":
            calorie_needs = self._bmr * 1.725
        elif self._activity_level == "athlete":
            calorie_needs = self._bmr * 1.9
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

    def estimated_grocery_budget(self, price_per_1000_kcal: float = 4) -> float:
        """price_per_1000_kcal:
            cheap diet = 2-3
            normal =4
            healthy/high protein = 5-7"""
        monthly_kcal = self.daily_kcal*30
        estimated = (monthly_kcal/1000)*price_per_1000_kcal
        return round(estimated, 2)

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
    @property
    def priority_of_activities(self):
    @property
    def priority_of_activities(self):
        activities = self.__dict__
        return dict(sorted(activities.items(), key=lambda x: x[1], reverse=True))
        """  activities = {  "rent" : self.rent,
        "groceries" : self.groceries,
        "insurance" : self.insurance,
        "bike_subscription" : self.bike_subscription,
        "gym_subscription" : self.gym_subscription,
        "going_out" : self.going_out,
        "hair_salon" : self.hair_salon,
        'hygenic_products': self.hygenic_products,
        "gifts" : self.gifts,
        "debts" : self.debts,
        "savings" : self.savings
    }

    sorted_activities = dict(
        sorted(activities.items(), key=lambda x: x[1], reverse=True)
    )

    return sorted_activities"""

    def compute_priorities(activities):
        total = sum (activities.items())
        budget = float(input ("Enter your total budget:"))
        remaining = budget
        for expense, amount in activities.values():
            if remaining >= amount:
                remaining -= amount
                print(f"Affordable - {expense}: {amount}")
            else:
                overspend =  amount - remaining
                print(f"Cannot afford - {expense}: {amount}- You're exceding your budget by {overspend}€")
    
        print(f"Total expenses : {total}")
        print(f"Remaining budget : {remaining}")

class Student: 
    """ this class focuss on academic buget """
    def __init__(self, device_cost=0, stationary_cost=0, printing_price=0, monthly_tuition_payment=0):
        self.device_cost = device_cost
        self.stationary_cost = stationary_cost
        self.printing_price = printing_price
        self.monthly_tuition_payment = monthly_tuition_payment
    """self at the begining is to store the info to the specific student"""
    """the =0 with each argument means that if the student doesnt put any values when the function is called then use 0 as a default """
    """this is good especially if somhow they are not the ones paying their monthly tuiton or if they dont use stationary cost(etc..)"""
    
=======
class Student: 
    """ this class focuss on academic buget """
    def __init__(self, device_cost=0, stationary_cost=0, printing_price=0, monthly_tuition_payment=0):
        self.device_cost = device_cost
        self.stationary_cost = stationary_cost
        self.printing_price = printing_price
        self.monthly_tuition_payment = monthly_tuition_payment
    """self at the begining is to store the info to the specific student"""
    """the =0 with each argument means that if the student doesnt put any values when the function is called then use 0 as a default """
    """this is good especially if somhow they are not the ones paying their monthly tuiton or if they dont use stationary cost(etc..)"""
    
>>>>>>> cb0fc2fc9f1f27c8571f30a30f71a943a75a6ff9
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
<<<<<<< HEAD
=======

class Budget:
    def __init__(self, overall_budget, rent_pct=0.5, food_pct=0.1,
                 social_pct=0.1, exercise_pct=0.1,
                 transport_pct=0.1, emergency_pct=0.1):
        if overall_budget < 0:
            raise ValueError("Overall budget cannot be negative")
        
        total_pct = (rent_pct + food_pct + social_pct +
                     exercise_pct + transport_pct + emergency_pct)
        if round(total_pct, 2) != 1.0:
            raise ValueError("Percentages must add up to 1")
        
        self.overall_budget = overall_budget 
        self.rent = overall_budget * rent_pct
        self.food_budget = overall_budget * food_pct
        self.socialising_budget = overall_budget * social_pct
        self.exercising_budget = overall_budget * exercise_pct
        self.transportation_budget = overall_budget * transport_pct
        self.emergency_fund = overall_budget * emergency_pct
>>>>>>> cb0fc2fc9f1f27c8571f30a30f71a943a75a6ff9

budget1 = Budget(budget) 
print("Your Rent Budget is €", budget1.rent)
print("Your Food Budget is €", budget1.food_budget)
print("Your Socialising Budget is €", budget1.socialising_budget)
print("Your Exercising Budget is €", budget1.exercising_budget)
print("Your Transportation Budget is €", budget1.transportation_budget)
print(budget1.emergency_fund, "€ is being added into your emergency fund")
<<<<<<< HEAD
=======

print("Your Transportation Budget is €", budget1.transportation_budget)
print(budget1.emergency_fund, "€ is being added into your emergency fund")
>>>>>>> cb0fc2fc9f1f27c8571f30a30f71a943a75a6ff9
