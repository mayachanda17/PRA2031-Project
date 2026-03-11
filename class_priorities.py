class Priorities :

     def__innit_ (self, rent, groceries, insurance, bike_subscription, gym_subscription, going_out, hair_salon, hygenic_products, gifts, debts, savings)
     self.rent = rent
     self.groceries = groceries 
     self. insurance = insurance
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
        "groceries" : price(
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
    
    @app.route('/pirorities', methods=["POST"] )
    def calculate_priorities():
        data = request.get_json()
        priorities = compute_priorities(data)
        return jsonify(priorities)
    
    if __Budget_calculator__ == '__main__':
        app.run(debug=True)
        app.py
        
print(priority_of_activities)
