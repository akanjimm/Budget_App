class Budget():
    "This is a budget app"
    def __init__(self, category_name):
        self.balance = 0
        self.category_name = category_name

    def deposit(self):
        amount_to_deposit = int(input(f"\nHow much would you like to deposit to {self.category_name} budget account? \n"))
        self.balance = self.balance + amount_to_deposit
        
        return f"₦{amount_to_deposit} was deposited to '{self.category_name} budget account' and current balance is ₦{self.balance}"

    def withdraw(self):
        amount_to_withdraw = int(input(f"\nHow much would you like to withdraw from {self.category_name} budget account? \n"))

        if amount_to_withdraw <= self.balance:
            self.balance = self.balance - amount_to_withdraw
            return f"₦{amount_to_withdraw} has been withdrawn from '{self.category_name} budget account' and current balance is ₦{self.balance}"

        else:
            return "Insufficient funds"

    def category_balance(self):
        return f"\nYour '{self.category_name} budget account' balance is ₦{self.balance}."

    def transfer(self, destination_category):
        amount_to_transfer = int(input(f"\nHow much would you like to transfer from {self.category_name} budget account? \n"))

        if amount_to_transfer <= self.balance:
            destination_category.balance += amount_to_transfer
            self.balance -= amount_to_transfer
            return f"₦{amount_to_transfer} was transferred to '{destination_category.category_name} budget account'. '{self.category_name} budget account' balance is ₦{self.balance}."
        else:
            return "Insufficient funds"


food = Budget("Food")
clothing = Budget("Clothing")
entertainment = Budget("Entertainment")
