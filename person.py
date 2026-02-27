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

   def estimated_grocery_budget(self, price_per_1000_kcal: float = 4) -> float:
        price_per_1000_kcal:
            cheap diet = 2-3
            normal =4
            healthy/high protein = 5-7
        monthly_kcal = daily_kcal*30
        estimated = (monthly_kcal/1000)*price_per_1000_kcal
        return round(estimated, 2)


