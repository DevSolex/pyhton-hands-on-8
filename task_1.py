class Registration:

    tuition = 50000

    def __init__(self, fname, lname, amount):
        self.firstname = fname
        self.lastname = lname
        self.amount_paid = amount

    def details(self):
        return f"firstname: {self.firstname}\nlastname: {self.lastname}\namount_paid: {self.amount_paid}"

    def balance(self):
        return self.tuition - self.amount_paid
    def balance_checker(self):
        if self.balance() == 0:
            return 'you have paid complete'
        else:
            return f'Your outstanding balance is {self.balance}'


joy = Registration('joy', 'tk', 20000)
tom = Registration('tom', 'ab', 50000)

print(joy.details())
print()
print(tom.details())
print()
print(tom.balance())
print()
print(tom.balance_checker())