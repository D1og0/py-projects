from importlib.metadata import files
from os import path

def checkAcc(email, password):
    print('a')

def main():
    print('')
    print(' Python checker')
    print(' Only for learning purposes (maybe)')

    try:
        accounts = 'accounts.txt'
        if (path.exists(accounts) and path.getsize(accounts) > 0):
            with open(accounts, "r") as filestream:
                for line in filestream:
                    accountArg = line.split(':')
                    args =  len(accountArg)
                    if (args == 3 or args == 2):\
                        email = accountArg[0]
                        #password = accountArg[1]
                        checkAcc(email, password)
        else:
            print('Accounts file is empty!')
            print('')
    except Exception as errorMsg:
        print('')
        print(errorMsg)
        print('An error occurred.. Saving progress...')
        print('')
        #writeToFile()


if __name__ == "__main__":
    main()