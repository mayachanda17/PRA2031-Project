class Priorities :
    def __init__ (self, income = 0, rent = 0, groceries = 0, insurance = 0, bike_subscription = 0, gym_subscription = 0, going_out = 0, hair_salon = 0, hygenic_products = 0, gifts = 0, debts = 0, savings = 0):
        self.income = income
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

        essentials = self.rent + self.groceries + self.insurance + self.bike_subscription
        remaining = self.income - essentials

        lifestyle = {
            "gym_subscription": self.gym_subscription,
            "going_out": self.going_out,
            "hair_salon": self.hair_salon,
            "hygenic_products": self.hygenic_products,
            "gifts": self.gifts,
            "debts": self.debts,
            "savings": self.savings
        }

        results = {}

        for category, amount in lifestyle.items():
            if remaining >= amount:
                results[category] = amount
                remaining -= amount
            else:
                results[category] = 0

        return results if results else {}
            
    def compute_priorities(self, activities):
        numeric_activities = {k: v for k, v in activities.items() if isinstance(v, (int, float))}
        total = sum(numeric_activities.values())

        if total == 0:
            return {k: 0 for k in numeric_activities}

        return {k: v / total for k, v in numeric_activities.items()}


