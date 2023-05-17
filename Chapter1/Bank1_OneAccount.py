# Non- OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = (input('What do you want to do? ')).lower()
    action = action[0]
    print()

    userPassword = input('Please enter the password: ')
    if userPassword == accountPassword:
        if action == 'b':
            print('Get balance: ')
            print(f'Your balance is: {accountBalance}')

        elif action == 'd':
            print('Deposit')
            userDepositAmount = int(input('Please enter amount to deposit: '))
            if userDepositAmount < 0:
                print('You cannot deposit a negative number')
            else:
                accountBalance += userDepositAmount
                print('Your new account balance is: ', userDepositAmount)

        elif action == 's':
            print('Show')
            print('       Name ', accountName)
            print('       Balance', accountBalance)
            print('       Password', accountPassword)

        elif action == 'q':
            break

        elif action == 'w':
            print('Withdraw')

            userWithdrawAmount = int(input('Please enter the amount to withdraw: '))

            if userWithdrawAmount < 0:
                print('You can not withdraw a negative number')

            elif userWithdrawAmount > accountBalance:
                print('You cannot withdraw more than you have in your account')

            else:
                accountBalance -= userWithdrawAmount
                print(f'Your new balance is {accountBalance}')

print('done')
