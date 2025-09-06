import random
class BankAccount:
    def __init__(self, account_name, balance, ispromo, isadmin, message):

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
                return f'SMS: Your account number is {self.account_number} and your balance is {self.balance}. You will receive an SMS shortly'
            elif self.message == 'Email':
                return f'Email: Your account number is {self.account_number} and your balance is {self.balance}. You will receive an Email shortly'
    def isfreeze(self, account_name):
        if self.isadmin == True:
            self.isfreeze = True
            return f'{account_name} account is frozen'
        else:
            return 'You are not authorized to freeze this account'

    def deposit(self, amount):
        if self.isfreeze:
            return "Can't perform this action Account is been frozen"
        else:
            self.balance += amount
            if self.message == 'SMS':
                return f'SMS: Your account number is {self.account_number} and your balance is {self.balance}. You will receive an SMS shortly'
            elif self.message == 'Email':
                return f'Email: Your account number is {self.account_number} and your balance is {self.balance}. You will receive an Email shortly'

    def withdraw(self, amount):
        if self.isfreeze:
            return "Can't perform this action Account is been frozen"
        if amount <= self.balance:
            self.balance -= amount
            if self.message == 'SMS':
                print(f'SMS: Your account number is {self.account_number} and your balance is {self.balance}. You will receive an SMS shortly')
            elif self.message == 'Email':
                print(f'Email: Your account number is {self.account_number} and your balance is {self.balance}. You will receive an Email shortly')
            return 'successful'
        else:
             return 'Insufficiet balance'

    def transfer(self, reciver, amount_to_send):
        if self.isfreeze:
            return "Can't perform this action Account is been frozen"
        if amount_to_send <= self.balance:
            tx = self.withdraw(amount_to_send)
            if tx == 'successful':
                reciver.deposit(amount_to_send)
                if self.message == 'SMS':
                    return f'SMS: You have sent {amount_to_send} to {reciver.account_name}. Your new balance is {self.balance}. You will receive an SMS shortly'
                elif self.message == 'Email':
                    return f'Email: You have sent {amount_to_send} to {reciver.account_name}. Your new balance is {self.balance}. You will receive an Email shortly'
            else:
                return 'Transfer failed'
        else:
            return 'Insufficient balance'

acc = BankAccount('solex', 1000, True, True, 'SMS')
solex = BankAccount('solo', 1900, True, False, 'Email')
print(solex.account_name)
print(solex.account_number)   
print(solex.balance) 
print(solex.ispromo)   
solex.deposit(1000)
print(solex.balance)
solex.withdraw(2000)
print(solex.balance)
solex.transfer(acc , 1500)
print(solex.balance)
acc.freeze('solo')
print(solex.deposit(1000))
