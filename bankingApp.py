users = [
    {'email':'myemail1@email.com', 'password':'password1', 'balance':200},
    {'email':'myemail2@email.com', 'password':'password2', 'balance':20}, 
    {'email':'myemail3@email.com', 'password':'password3', 'balance':10},
    {'email':'myemail4@email.com', 'password':'password4', 'balance':0},
    {'email':'myemail5@email.com', 'password':'password5', 'balance':100}
        ]


def banking():
    print("press 1: create account \npress 2: transaction\n")
    userschoice = input("Enter: ")
    if userschoice == str(1):
        create_account()
    elif userschoice == str(2):
        transaction()
        
    elif userschoice == '0':
        quit()
    else:
        print('Your Entry is Invalid Please Try agin  ')
        return banking()


# This function checks if user with a given attribute and corresponding value exist
def userExist(attr, value):
    for user in users:
        if user[attr] == value:
            return user
    return False

def create_account():
    print("WELCOME TO SBA BANK ACCOUNT CREATING PROCESS")
    print("IT'S EVERY SECURED AND EASY\n")

    email = input("PLEASE ENTER YOUR EMAIL ADDRESS\n ")
    while(True):
        if not userExist('email',email.lower()):
            break
        else:
            print('Sorry this email already exist, choose another one.\n')
            email = input("PLEASE ENTER YOUR EMAIL ADDRESS\n ")


    password = input("PLEASE ENTER YOUR PASSWORD\n ")

    while(True):
        if len(password) > 6 :
            break
        else:
            print('password must be six characters or more \n')
            password = input("PLEASE ENTER YOUR PASSWORD\n ")

    add_new_user = {'email':email.lower(), 'password':password, 'balance': 0.0}
    users.append(add_new_user)
    print('Account was created successfully! \n')
    transaction()

def check_balance(user):
    print('Your account balance is {} \n'.format(user['balance']))
    transaction()

def deposit_money(user):
    # amount to be deposited
    amount = input('Please enter the Amount you want deposit \n')
    while(True) :
        try:
            deposit_amount = float(amount)
            if deposit_amount > 0.0:
                break
            else:
                print('You have entered invalid amount\n')
                amount = input('Please enter the Amount you want deposit \n')
        except ValueError:
            print('You have entered invalid amount\n')
            amount = input('please enter the Amount you want deposit \n')
    new_balance = float(user['balance']) + deposit_amount
    print('you successfuly made a deposit of {deposit}, your new account balance is now {balance} \n'.format(deposit = deposit_amount, balance = new_balance))
    user['balance'] = new_balance
    transaction()

def withdraw(user):
    amount = input('Please enter the amount you want to withdraw\n')
    while(True) :
        try:
            withdraw_amount = float(amount)
            if withdraw_amount > 0.0:
                break
            else:
                print('You have entered invalid amount\n')
                amount = input('please enter the amount you want to withdraw\n')
        except ValueError:
            print('You have entered invalid amount\n')
            amount = input('please enter the amount you want to withdraw\n')
    if user['balance'] == 0.0:
        print('Sorry You have an insufficent balance')
        deposit_money(user)
    elif user['balance'] < withdraw_amount:
        print('Sorry You have an insufficent balance\n')
    else:
        new_balance = float(user['balance']) - withdraw_amount
        print('your have successfully withdrawn {withdrawn_amount}, your new balance is {balance} \n'.format(withdrawn_amount = withdraw_amount, balance = new_balance))
        user['balance'] = new_balance
        transaction()

def tranfer(user):
    amount = input('Please enter the amount you want to transfer\n')
    while(True) :
        try:
            transfer_amount = float(amount)
            if transfer_amount > 0.0:
                break
            else:
                print('You have entered invalid amount\n')
                amount = input('please enter the amount you want to transfer\n')
        except ValueError:
            print('You have entered invalid amount\n')
            amount = input('please enter the amount you want to transfer\n')
    if float(user['balance']) < transfer_amount:
        print('sorry you have an insufficent balance')
    else:
        receiver = input('Please enter the beneficiary\'s email address \n')
        while(True):
            beneficiary = userExist('email',receiver.lower())

            if beneficiary:
                break
            print(' sorry No account has that email Address\n')
            receiver = input('Please enter beneficiaries email address\n')
        
        beneficiary_balance = float(beneficiary['balance']) + transfer_amount
        sender_balance = user['balance'] - transfer_amount
        beneficiary['balance'] = beneficiary_balance
        user['balance'] = sender_balance
        print('you successfully transfered {sent_amount} to {reciever}, your balance is now {new_balance} \n'.format(sent_amount = transfer_amount, reciever = beneficiary['email'], new_balance = user['balance']))
        transaction()

def transaction():

    print("WELCOME, OUR DEAR VALUED CUSTOMER, WE ARE HERE TO SERVE YOU BETTER")
    print("WHAT TRANSACTIONS DO YOU WANT TO PERFORM TODAY\n")

    password = input("PLEASE ENTER YOUR PASSWORD\n ")
    the_user = userExist('password', password)

    if not the_user:
        print('Sorry Your password is incorrect!')
        banking()
    else:
        
        user_choice = input('press 1: Check Balance\npress 2: Deposit\npress 3: Withdraw\npress 4: Transfer\npress 0: Go back to Main menu\n')
        if user_choice == '0':
            banking()
        elif user_choice == str(1):
            check_balance(the_user)
        elif user_choice == str(2):
            deposit_money(the_user)
        elif user_choice == str(3):
            withdraw(the_user)
        elif user_choice == str(4):
            tranfer(the_user)
        else:
            print('Your Entry is Invalid Please Try agin  ')
            transaction()


banking()