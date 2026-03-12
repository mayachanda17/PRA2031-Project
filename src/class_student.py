class Student: 
 """ Gather budget information about the user if a student"""
    def __init__(self, device_cost=0, stationary_cost=0, printing_price=0, monthly_tuition_payment=0):
        self.device_cost = device_cost
        self.stationary_cost = stationary_cost
        self.printing_price = printing_price
        self.monthly_tuition_payment = monthly_tuition_payment
    
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
        
    def tuition_fee (self):
        monthly_tuition= input("\n do you pay yourself a monthly tuiton (Y/N): ")
        if monthly_tuition.upper()== "Y":
            student1.monthly_tuition_payment= float(input("what is your monthly university payment?: "))
        else:
            student1.monthly_tuition_payment= 0
        monthly_tuition = self.monthly_tuition_payment
    def total_monthly_academic_costs (self):
        total_monthly_academic_costs= (self.device_cost+self.stationary_cost +self.printing_price +self.monthly_tuition_payment)
        return total_monthly_academic_costs
