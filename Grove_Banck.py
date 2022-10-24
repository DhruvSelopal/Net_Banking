print("Welcome to the Grove street bank")
print("Please use alphabets only")
total_amount = 0
running = True
loan = False
amount_to_pay = 0
while running:
    print('''
    a) Deposit money
    b) Withdraw money
    c) Learn about the loan
    d) Take a loan
    e) Pay your loan
    f) Check your balance
    h) Exit''')
    cmd = input("What feature would you like to use: ").lower()
    if cmd == 'a':
        try:
            total_amount += int(input("Amount you wanna deposit: "))
            print("Amount deposited")
        except ValueError:
            print("Amount cannot be alphabets.")
    elif cmd == 'b':
        try:
            withdraw_amount = int(input("Amount you wanna Withdraw: "))
            if withdraw_amount > total_amount:
                print("Insufficient balance")
            else:
                total_amount -= withdraw_amount
                print(f"You withdrawal {withdraw_amount}")
        except ValueError:
            print("Amount cannot be alphabets.")
    elif cmd == 'c':
        print('''
        * We offer loan with low interest
        * But if you dont pay within the given time CJ will be after you.
        * For loan greater then 10,000 , interest will be 20% percent the price .
        * For loan less then 10,000 ,  interest will be 10% the price.
        * You have to deposit something precious like your ak or some ZR 350.
        ''')
    elif cmd == 'd':
        if loan:
            print("You already have a loan going on ")
            print(f"You have to pay {amount_to_pay} money.")
            print("Press e to pay the loan")
        else:
            try:
                loan_money = int(input("How much amount you wanna have: "))
                if loan_money > 10000:
                    amount_to_pay += (loan_money*0.2) + loan_money
                    print(f"You have to pay {amount_to_pay} by the end of month.")
                else:
                    amount_to_pay += (loan_money*0.1) + loan_money
                    print(f"You have to pay {amount_to_pay} by the end of week.")
                loan = True
            except ValueError:
                print("Please use digits here")
    elif cmd == 'e':
        try:
            pay = int(input("How much would you like to pay: "))
            if pay > amount_to_pay:
                print("Your loan has been paid.")
                print("As for the extra tip you can now be the part of the hood.")
                loan = False
            elif pay == amount_to_pay:
                print("Your loan is off")
                loan = False
            else:
                amount_to_pay -= pay
                print(f"You have {amount_to_pay} left to pay.")
        except ValueError:
            print("Please use digits only")
    elif cmd == 'f':
        print(f"Your balance is {total_amount}")
    elif cmd == 'h':
        running = False
print("THANK YOU FOR USING GROVE BANK")

