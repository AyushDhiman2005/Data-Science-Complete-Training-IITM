class Bank_Account():

    def __init__(self,name,num,balance):
        self.account_holder_name = name
        self.account_number=num
        self.__balance=balance
        print("Account Established Successfully!")
    
    def deposit(self,amount):
        self.__balance = self.__balance+amount
        print(f"Amount {amount} deposited successfully!")

    def withdraw(self,amount):
        if amount>self.__balance:
            print(f"Cannot withdraw {amount} due to Insufficient Balance!")
        else:
            self.__balance = self.__balance-amount

    def check_balance(self):
        print(f"Your current balance is {self.__balance}")
    
john=Bank_Account("John",102089,20000)
john.withdraw(25000)
john.check_balance()
john.deposit(10000)
john.withdraw(25000)
john.check_balance()