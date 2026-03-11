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

budget1 = Budget(budget) 
print("Your Rent Budget is €", budget1.rent)
print("Your Food Budget is €", budget1.food_budget)
print("Your Socialising Budget is €", budget1.socialising_budget)
print("Your Exercising Budget is €", budget1.exercising_budget)
print("Your Transportation Budget is €", budget1.transportation_budget)
print(budget1.emergency_fund, "€ is being added into your emergency fund")

print("Your Transportation Budget is €", budget1.transportation_budget)
print(budget1.emergency_fund, "€ is being added into your emergency fund")
