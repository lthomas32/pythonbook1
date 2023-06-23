from Bank import *

def main():
    oBank = Bank('9-5', 'Medical Lake', '123-456-7890')

    while True:
        print()
        print('To get an account balance, press b')
        print('To open an account, press o')
        print('To close an account, press c')
        print('To make a deposit, press d')
        print('To get bank information, press i')
        print('To show all accounts, press s')
        print('To make a withdrawal, press w')
        print('To quit, press q')

        action = input('What do you want to do? ')
        action = action.lower()
        action = action[0]
        print()

        try:
            if action == 'b':
                oBank.balance()
            elif action == 'c':
                oBank.closeAccount()
            elif action ==  'd':
                oBank.deposit()
            elif action == 'i':
                oBank.getInfo()
            elif action == 'o':
                oBank.openAccount()
            elif action == 's':
                oBank.show()
            elif action == 'w':
                oBank.withdraw()
            elif action == 'q':
                break
        except AbortTransaction as error:
            print(error)

    print('GoodBye')

if __name__ == "__main__":
    main()

