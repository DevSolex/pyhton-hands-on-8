import random
class BankAccount:
    def __init__(self, account_name:str, balance:float=0, ispromo:bool=False, isadmin:bool=False, message: str ='SMS'): 

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

    def freeze(self, target_account: 'BankAccount'):
        if self.isadmin == True:
            if target_account.account_name != self.account_name:
                target_account.isfreeze = True
                print(f'Dear {target_account.account_name} your account is frozen')
        else:
            print(f'You are not an admin to freeze {target_account.account_name} account')

    def unfreeze(self, target_account: 'BankAccount'):
        if self.isadmin == True:
            if target_account.account_name == self.freeze:
                target_account.isfreeze = False
                print(f'Dear {target_account.account_name} your account has been unfreeze.')
        else:
            print(f"you are not an admin to unfreeze {target_account.account_name} account.")



    def deposit(self, amount: float):
        if self.isfreeze:
            print(f"Dear {self.account_name} you can't deposit your Account is been frozen")
        else:
            self.balance += amount
            if self.message == 'SMS':
                print(f'SMS: Dear {self.account_name} Your account has been credited with {amount}. Your new balance is {self.balance}.')
            elif self.message == 'Email':
                print(f'Email: Dear {self.account_name} Your account has been credited with {amount}. Your new balance is {self.balance}.')




    def withdraw(self, amount: float):
        if self.isfreeze == True:
            return f"Dear {self.account_name} you can't withdraw your Account is been frozen"
        
        if amount <= self.balance:
            self.balance -= amount
            if self.message == 'SMS':
                print(f'SMS: Dear {self.account_name} Your account has been debited with {amount}. Your new balance is {self.balance}.')
            elif self.message == 'Email':
                print(f'Email: Dear {self.account_name} Your account has been debited with {amount}. Your new balance is {self.balance}.')
            return 'successful'
        else:
            print('Insufficient balance')




    def transfer(self, reciver: 'BankAccount', amount_to_send: float):
        if self.isfreeze == True:
            print(f"Dear {self.account_name} you can't make transfer your Account is been frozen")

        if amount_to_send <= self.balance:
            tx = self.withdraw(amount_to_send)
            if tx == 'successful':
                reciver.deposit(amount_to_send)
                print(f'Transferred of {amount_to_send} to {reciver.account_name} successfully')
            else:
                return 'Transfer failed'
        else:
            return 'Insufficient balance'




