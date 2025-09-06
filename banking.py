import random
class BankAccount:
    def __init__(self, account_name, balance=0, ispromo=False, isadmin=False, message='SMS'):

        self.account_name = account_name
        self.account_number = random.randint(000000000, 999999999)
        self.balance = balance
        self.promo_price = 2000
        self.ispromo = ispromo
        self.isadmin = isadmin
        self.message = message
        self.isfreeze = False

        if self.ispromo == True:
            self.balance += self.promo_price
            self.account_number
            if self.message == 'SMS':
                print(f'SMS: Dear {self.account_name} Your account number is {self.account_number} and your balance is {self.balance}.')
            elif self.message == 'Email':
                print(f'Email: Dear {self.account_name} Your account number is {self.account_number} and your balance is {self.balance}.')

    def freeze(self, account_name):
        if self.isadmin == True:
            self.isfreeze = True
            print(f'Dear {account_name} your account is frozen')
        else:
            print(f'You are not an admin to freeze {account_name} account')




    def deposit(self, amount):
        if self.isfreeze:
            print("Can't deposit your Account is been frozen")
        else:
            self.balance += amount
            if self.message == 'SMS':
                print(f'SMS: Dear {self.account_name} Your account has been credited with {amount}. Your new balance is {self.balance}.')
            elif self.message == 'Email':
                print(f'Email: Dear {self.account_name} Your account has been credited with {amount}. Your new balance is {self.balance}.')




    def withdraw(self, amount):
        if self.isfreeze:
            return "Can't withdraw your Account is been frozen"
        else:
            if amount <= self.balance:
                self.balance -= amount
                if self.message == 'SMS':
                    print(f'SMS: Dear {self.account_name} Your account has been debited with {amount}. Your new balance is {self.balance}.')
                elif self.message == 'Email':
                    print(f'Email: Dear {self.account_name} Your account has been debited with {amount}. Your new balance is {self.balance}.')
                return 'successful'
            else:
                print('Insufficient balance')




    def transfer(self, reciver, amount_to_send):
        if self.freeze:
            print("Can't make transfer your Account is been frozen")
        else:
            if amount_to_send <= self.balance:
                tx = self.withdraw(amount_to_send)
                if tx == 'successful':
                    reciver.deposit(amount_to_send)
                    if self.message == 'SMS':
                        print(f'SMS: Dear {self.account_name} Your account has been debited with {amount_to_send} to {reciver.account_name}. Your new balance is {self.balance}.')
                    elif self.message == 'Email':
                        print(f'Email: Dear {self.account_name} Your account has been debited with {amount_to_send} to {reciver.account_name}. Your new balance is {self.balance}.')
                else:
                    return 'Transfer failed'
            else:
                return 'Insufficient balance'




acc = BankAccount('solex', 1000, True, True, 'SMS')
solex = BankAccount('solo', 1900, True, False, 'Email')
acc.freeze('solo')
solex.deposit(1000)

