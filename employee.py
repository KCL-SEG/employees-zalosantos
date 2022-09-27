"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hourly, monthly, hours, contract, numberOfContracts, commission):
        self.name = name
        self.hourly = hourly
        self.monthly = monthly
        self.hours = hours
        self.commission = commission
        self.numberOfContracts = numberOfContracts
        self.contract = contract

    def get_pay(self):

        x = self.hourly * self.hours + self.monthly + (self.contract * self.numberOfContracts) + self.commission
        return self.hourly * self.hours + self.monthly + (self.contract * self.numberOfContracts) + self.commission

    def get_hours(self):
        if self.hours != 0:
            return "works on a contract of " + self.hours + " at "
        else:
            return ""

    def get_hourly(self):
        if self.hourly != 0:
            return  self.hourly + "/hour."
        else:
            return ""

    def get_monthly(self):
        if self.monthly != 0:
            return "works on a monthly salary of " + self.monthly + "."
        else:
            return ""

    def get_numberOfContracts(self):
        if self.numberOfContracts != 0:
            return "and receives a commission for " + self.numberOfContracts + " at "
        else:
            return ""

    def get_contract(self):
        if self.contract != 0:
            return self.contract + "/contract."
        else:
            return ""

    def get_commission(self):
        if self.commission != 0:
            return "and receives a bonus commission of " +self.commision + "."
        else:
            return ""

    def __str__(self):
        return self.name + get_hours(self) + get_hourly(self)+ get_monthly(self) + get_contract(self) + get_numberOfContracts(self) + get_commission(self) + "  Their total pay is " + get_pay(self) + "."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',0,4000,0,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',25,0,100,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',0,3000,0,200,4,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',25,0,150,220,3,0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',0,2000,0,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',30,0,120,0,0,600)
