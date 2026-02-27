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
       activities = {  "rent" : self.rent,
        "groceries" : self.groceries,
        "insurance" : self.insurance,
        "bike_subscription" : self.bike_subscription,
        "gym_subscription" : self.gym_subscription,
        "going_out" : self.going_out,
        "hair_salon" : self.hair_salon,
        'hygenic_products': self.hygenic_products,
        "gifts" : self.gifts,
        "debts" : self.debts,
        "savings" : self.savings}
    sorted_activities = dict(sorted(activities.items(), key=lambda x: x[1], reverse=True))
    return sorted_activities

   def compute_priorities(activities):
        total = sum (activities.values())
        budget = float(input ("Enter your total budget:"))
        remaining = budget
       for expense, amount in activites.items():
       if remaining >= amount:
           remaining -= amount
           print(f"Affordable - {expense}: {amount}")
      else:
          overspend = spent_so_far + amount - total_budget
           print(f"Cannot afford - {expense}: {amount}- You're exceding your budget by {overspend}€")
    
      print(f"Total expenses : {Total}")
      print(f"Remaining budget : {reamining}")
