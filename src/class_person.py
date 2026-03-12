class Person:
    def __init__(self, name, age, height, weight, gender, activity_level):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.activity_level = activity_level


    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age


    @property
    def height(self):
        return self._height
    @height.setter
    def height (self, height):
        if height < 0 or height > 272:
            raise ValueError("Height cannot be negative or greater than 272 cm")
        self._height = height


    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be greater than 0")
        self._weight = weight


    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        gender = gender.strip().lower()
        if gender != "man" and gender != "woman":
            raise ValueError("For this program, you must enter sex as either MAN or WOMAN")
        self._gender = gender


    @property
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def bmi_category(self):
        if self.bmi < 18.5:
            return "You are underweight"
        elif self.bmi < 25:
            return "You are normal weight"
        elif self.bmi < 30:
            return "You are overweight"
        else:   
            return "You are obese"


    @property
    def activity_level (self):
        return self._activity_level

    @activity_level.setter
    def activity_level(self, activity_level):
        if activity_level < 1 or activity_level > 5:
            raise ValueError("Activity level must be between 1 and 5")
        self._activity_level = activity_level


    @property
    def bmr (self):
        if self.gender == "man":
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161


    @property
    def calorie_needs(self):
        #Step 1: Multiply BMR by activity level factor
        if self.activity_level == 1:
            calories = self.bmr * 1.2
        elif self.activity_level == 2:
            calories = self.bmr * 1.375
        elif self.activity_level == 3:
            calories = self.bmr * 1.55
        elif self.activity_level == 4:
            calories = self.bmr * 1.725
        elif self.activity_level == 5:
            calories = self.bmr * 1.9
        
        #Step 2 = Adjust for age ( depending on metabolism slowing down with age)
        if self.age < 18: 
            calories *= 1.15 # growing teens need 15% more calories
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
            calories *= 0.88
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
        monthly_kcal = self.calorie_needs * 30
        estimated = (monthly_kcal / 1000) * price_per_1000_kcal
        return round(estimated, 2)



