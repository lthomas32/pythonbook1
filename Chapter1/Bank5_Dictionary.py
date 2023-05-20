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
        print ('Incorrect Password!')
        return None
    return thisAccountDict['balance']

def deposit(accountNumber, amount, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print ('Incorrect Password!')
        return None
    if amount <= 0:
        print('You didn\'t deposit any money')
        return None
    thisAccountDict['balance'] += deposit
    print('Your new account balance is ', thisAccountDict['balance'])
    return thisAccountDict['balance']


def withdraw(accountNumber,amount, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print ('Incorrect Password!')
        return None
    newBalance = thisAccountDict['balance'] - amount
    if newBalance < 0:
        print('You tried to withdraw to much money ')
        return None
    thisAccountDict['balance'] = newBalance
    print(f'Your new balance is ${newBalance}')
    return newBalance



    





