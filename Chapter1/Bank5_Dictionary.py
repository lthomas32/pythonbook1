# Non -OOP Bank
# Version 5
# Any number of accounts with a list of dictionaries

accountsList = []


def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountsList.append(newAccountDict)


def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('        Name', thisAccountDict['name'])
    print('        Balance', thisAccountDict['balance'])
    print('        Password', thisAccountDict['password'])


def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect Password!')
        return None
    return thisAccountDict['balance']


def deposit(accountNumber, amount, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect Password!')
        return None
    if amount <= 0:
        print('You didn\'t deposit any money')
        return None

    thisAccountDict['balance'] += amount
    print('Your new account balance is ', thisAccountDict['balance'])
    return thisAccountDict['balance']


def withdraw(accountNumber, amount, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect Password!')
        return None
    newBalance = thisAccountDict['balance'] - amount
    if newBalance < 0:
        print('You tried to withdraw to much money ')
        return None
    thisAccountDict['balance'] = newBalance
    print(f'Your new balance is ${newBalance}')
    return newBalance


print("Joe's account is account number: ", len(accountsList))
newAccount("Joe", 100, "soup")

print("Mary's account is account number: ", len(accountsList))
newAccount("Mary", 12345, "nuts")

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]

    if action == 'b':
        print('Get Balance: ')
        userAccountNumber = int(input("Please enter your account number: "))
        userPassword = input("Please enter the password: ")
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is: ', theBalance)


    elif action == 'd':
        print('Deposit: ')
        userAccountNumber = int(input("Please enter the account number: "))
        userDepositAmount = int(input("Please enter the amount to deposit: "))
        userPassword = input("Please enter the password: ")
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)

    elif action == 'n':
        print("New Account: ")
        userName = input("What is your name? ")
        userStartingAmount = input("What is the amount of your initial deposit? ")
        userStartingAmount = int(userStartingAmount)
        userPassword - input("What password would you like to use for this account")

        userAccountNumber = len(accountsList)
        newAccount(userName,userStartingAmount, userPassword)
        print('Your new account number: ', userAccountNumber)

    #TODO Make option w for Withdrawel


    #TODO Make option s for Show All Accounts


    #TODO Make option q for quit aka break

