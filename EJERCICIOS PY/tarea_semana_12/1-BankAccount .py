
class BankAccount:
    def __init__(self, balance):
        self._balance=balance

    def deposit(self, amount):
        if amount > 0:
            self._balance+=amount
            print("your deposit was made successfully")


    def withdrawal(self, amount):
        if self._balance>=amount and amount>0:
            self._balance-=amount
            print(f"your withdrawal was made successfully your new balance is: {self._balance}")
        else:
            print("Insufficient funds or invalid amount")


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance=min_balance

    def withdrawal(self,amount):
        if self._balance>=amount and amount>0 and self._balance-amount>= self.min_balance:
            self._balance-=amount
            print(f"your withdrawal was made successfully your new balance is: {self._balance}")
        else:
          raise ValueError("The withdrawal would leave the balance below the minimum allowed.")

savings=SavingsAccount(500,100)
try:
    savings.withdrawal(400)
except ValueError as e:
    print(f"error {e}")