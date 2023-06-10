class Account():
    #this is basically the constructor and parameters
    def __int__(self,name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("This is the incorrect password")
            return None
        if amountToDeposit < 0:
            print("You can not deposit an negative Number")
            return None
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("This is the incorrect password")
            return None
        if amountToWithdraw < 0 or amountToWithdraw > self.balance:
            print("You can not do this")
            return None
        self.balance -= amountToWithdraw
        return self.balance


    def getBalance(self, password):
        if password != self.password:
            print("This is the incorrect password")
        return self.balance