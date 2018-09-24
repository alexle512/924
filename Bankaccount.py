class BankAccount:
    def __init__(self,first_name, middle_name, last_name, balance,account_type,status):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.balance = balance
        self.account_type = account_type
        self.status = status
       

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        penalty = 35
        if self.balance - amount < 0:
            self.balance -= (amount + penalty)
        
        else:
            self.balance -= amount
        return self.balance
        

    def get_balance(self): 
        return self.balance


def main():
    customer = BankAccount('Alex',"Tran","Le", 1000 ,"checking","open")
    print(customer.get_balance())
    customer.deposit(0)
    customer.withdraw(1005)
    print(customer.get_balance())

main()