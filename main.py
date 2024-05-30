from registerlogin import *
from dep_bal import*
from spin import*
while(True):
    print("WELCOME TO SPIN WHEEL")
    print("*"*50)
    time.sleep(1)
    print("REGISTER OR LOGIN TO SPIN THE WHEEL")
    print("-"*50)
    time.sleep(1)
    print("\n\n 1.Register  2.Login")
    op = int(input("Enter your option:"))
    if op == 1:
        uname = input("Enter Username:")
        password = input("Enter Password:")
        balance = int(input("Balance:"))
        rtn = register(uname, password, balance)
        if rtn:
            print("ACCOUNT SUCCESFULLY CREATED")
            break
        else:
            print("USER ALREADY EXIXTS")

    elif op == 2:
        uname = input("Enter Username:")
        password = input("Enter Password:")
        rtn = login(uname, password)
        if rtn:
            print("LOGIN SUCCESSFULL")
            break
        else:
            print("USERNAME OR PASSWORD DOSES NOT MATCH")
    else:
        print("INVALID OPTION")
while(True):
    print("\n\n 1.Deposit 2.Check Balance 3.Spin 4.Exit")
    op = int(input("Enter your option:"))
    if op == 1:
        balance = (input("ENTER AMOUNT TO DEPOSIT:"))
        deposit(uname, balance)
        print("AMOUNT SUCCESSFULLY DEPOSITED")
    elif op == 2:
        rtn = checkbal(uname)
        print(f"AVAILABLE BALANCE:{rtn}")
    elif op == 3:
        bet = int(input("Enter the amount to Bet:"))
        bal = checkbal(uname)
        if bet > bal:
            print("no sufficient balance")
            continue
        s1, s2, s3 = spin()
        points, bal = check(s1, s2, s3, bet, bal)
        update(uname, bal)
        display(s1, s2, s3, points, bal)

    elif op == 4:
        break
    else:
        print("Invalid Option")
        