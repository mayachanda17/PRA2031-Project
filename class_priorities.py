class Priorities :

    def __init__ (self, income, rent, groceries, insurance, bike_subscription, gym_subscription, going_out, hair_salon, hygenic_products, gifts, debts, savings):
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
                remaining -= amount
                results[category] = amount 
            else:
                results[category] = "You don't have enough money for this category."
                return results
            
    def compute_priorities(self,activities):
        total = sum (activities.values())
        if total == 0:
            return  {k: 0 for k in activities}
        return  {k: v / total for k, v in activities.items()}
        
my_budget = Priorities(
    rent=float("Enter your rent price:"),
    groceries = float("Enter your groceries:"),
    insurance = float("Enter your insurance price:"),
    bike_subscription = float("Enter your bike subscription price:"),
    gym_subscription = float("Enter your gym subscription price:"),
    going_out = float("Enter your going out price:"),
    hair_salon = float("Enter your hair salon price:"),
    hygenic_products = float("Enter your hygenic products price:"),
    gifts = float("Enter your prefered price for gifts:"),
    debts = float("Enter your debts price:"),
    savings = float("Enter your prefered savings price:")

    )
print(my_budget.priority_of_activities())

