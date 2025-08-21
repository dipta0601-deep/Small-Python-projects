'''
ATM Machine Simulation
ATM class with methods: insert_card(), enter_pin(), withdraw(), deposit().
Secure private balance.
Raise exceptions for invalid PIN or insufficient balance.
'''

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance
        self.__authenticated = False

    def insert_card(self):
        print("card inserted successfully,\n please enter your pin")

    def enter_pin(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("You have entered a correcect Pin, Logged in")
        else:
            raise ValueError("You have enterer an incorrect pin")

    def withdraw(self, amount):
        if not self.__authenticated:
            raise PermissionError("Please enter a correct pin first")
        if amount <= 0:
            raise ValueError("Enter a positive amount")
        if amount > self.__balance:
            raise ValueError("Insufficient bank balance")
        self.__balance -= amount
        print(f"Withdrawn {amount} remaining balance rs. {self.__balance}")

    def deposit(self, amount):
        if not self.__authenticated:
            raise PermissionError("Please enter a correct pin first")
        if amount <= 0:
            raise ValueError("Please enter a positive amount")
        self.__balance += amount
        print(f"Amount Rs. {amount} has been deposited. Total balance rs. {self.__balance}")


    def show_balance(self):
        if not self.__authenticated:
            raise PermissionError("Please enter a correct pin")
        print(f'Current Balance Rs. => {self.__balance}')
        return self.__balance

ATM = ATM("9123", 100000)
ATM.enter_pin(input("Enter the correct pin: "))
ATM.deposit(int(input("Enter amount to deposit: ")))
ATM.withdraw(int(input("Enter the withdrawl amount: ")))
ATM.show_balance()
