from class_person import Person
class Budget:
    """Divide the monthly budget of the user between the different activities"""
    def __init__(self, priorities, student=None):
        self.priorities = priorities
        self.student = student
        self.income = priorities.income

   # if self.income < 0:
      #  raise ValueError("Income cannot be negative")

    def monthly_priority_costs(self):
        return {
            "rent": self.priorities.rent,
            "groceries": self.priorities.groceries,
            "insurance": self.priorities.insurance,
            "bike_subscription": self.priorities.bike_subscription,
            "gym_subscription": self.priorities.gym_subscription,
            "going_out": self.priorities.going_out,
            "hair_salon": self.priorities.hair_salon,
            "hygenic_products": self.priorities.hygenic_products,
            "gifts": self.priorities.gifts,
            "debts": self.priorities.debts,
            "savings": self.priorities.savings,
        }

    def total_priority_costs(self):
        return sum(self.monthly_priority_costs().values())

    def total_student_costs(self):
        if self.student is None:
            return 0
        return self.student.total_monthly_academic_costs()

    def total_expenses(self):
        return self.total_priority_costs() + self.total_student_costs()

    def remaining_budget(self):
        return self.income - self.total_expenses()

    def summary(self):
        return {
            "income": self.income,
            "priority_costs": self.total_priority_costs(),
            "student_costs": self.total_student_costs(),
            "total_expenses": self.total_expenses(),
            "remaining_budget": self.remaining_budget(),
        }
