class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)
        
acc = BankAccount(1000)  
while True:

    print("\n1 Check Balance")
    print("2 Deposit")
    print("3 Withdraw")
    print("4 Exit")

    choice=input("enter the input:")
    if choice=="1":
        acc.show_balance()
    elif choice=="2":
        amount=int(input("enter the deposite amount:"))
        acc.deposit(amount)
    elif choice=="3":
        wit=int(input("enter withdraw amount:"))
        acc.withdraw(wit)
    elif choice=="4":
        print("thank you...")
        break
    else:
        print("invalid-option....")
    
