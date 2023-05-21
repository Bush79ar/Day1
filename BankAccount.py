class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening  = date_of_opening 
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("can not.")
        else:
            self.balance -= amount
            print(f"${amount}  withdrawn from your account.")
            
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
        
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance: ${self.balance}\n")   


s_1 = BankAccount(2345, "01-01-2011", 1000, "Bushra")
s_2 = BankAccount(1234, "11-03-2011", 2000, "ccc")
s_3 = BankAccount(2312, "12-01-2009", 3000, "bbbb")
s_4 = BankAccount(1395, "01-01-2011", 3000, "jjj")
s_5 = BankAccount(6345, "01-05-2011", 4000, "ppp")

print("Customer Details:")
s_1.print_customer_details()
s_2.print_customer_details()
s_3.print_customer_details()
s_4.print_customer_details()
s_4.print_customer_details()

print("===")
s_4.print_customer_details()
s_4.deposit(1000)
s_4.check_balance()
s_4.withdraw(5000)
s_4.withdraw(3400)
s_4.check_balance()