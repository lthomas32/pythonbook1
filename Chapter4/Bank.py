from Account import *


class Bank:
    def __init__(self, hours, address, phone):
        self.accountDict = {}
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone


    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountDict[newAccountNumber] = oAccount
        self.nextAccountNumber += 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user')
        userStartingPoint = int(input('What is the starting balance for this account'))
        userPassword = input('What is the password you want for this account')

        userAccountNumber = self.createAccount(userName,userStartingPoint,userPassword)
        print('Your new account number is ', userAccountNumber, '\n')

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        print('Here is your balance ', oAccount.getBalance())
        del self.accountDict[userAccountNumber]
        print("Your account is now closed")

    def askForValidAccountNumber(self):
        try:
            accountNumber = int(input('What is your account number '))
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        if accountNumber not in self.accountDict:
            raise AbortTransaction("There is no account")
        return accountNumber
    def askForValidPassword(self, account):
        if not isinstance(account,Account):
            raise AbortTransaction("Not a valid account")
        password = input("What is your password?")
        account.checkPassword(password)


    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    def balance(self ):
        oAccount = self.getUsersAccount()
        return oAccount.getBalance()


    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        depositAmount = input('Please enter an amount to deposit')
        theBalance = oAccount.deposit(depositAmount)
        print(f"Deposited: {depositAmount}\nYour new balance is {theBalance}")

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        withdrawAmount = input('Please enter an amount to withdraw')
        theBalance = oAccount.withdraw(withdrawAmount)
        print(f"Withdrawn: {withdrawAmount}\nYour new balance is {theBalance}")

    def getInfo(self):
        print("Hours: ", self.hours)
        print("Address: ", self.address)
        print('Phone, ', self.phone)

    def show(self):
        print('*** Show ***')
        print('(This would typically require an admin password)')
        for userAccountNumber in self.accountDict:
            oAccount = self.accountDict[userAccountNumber]
            print('Account: ', userAccountNumber)
            oAccount.show()
            print()

