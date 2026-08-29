class Bank:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu (self):
        user_input = input("""
        press 1 for set pin
        press 2 for reset pin
        press 3 for balance inquiry
        press 4 for money withdrawl
        press 5 to exit: """)


        if user_input == '1':
            self.set_pin()
        elif user_input == '2':
            self.reset_pin()
        elif user_input == '3':
            self.view_balance()
        elif user_input == '4':
            self.money_withwraval()
        else:
            exit()
    
   


    def set_pin (self):
        create_pin = input('create your first pin: ')
        self.pin = create_pin
        deposit = int(input('deposit your amount: '))
        if deposit >= 5000:
            self.balance = deposit
        else:
            print('minimum 5000 deposit require to open new account')
            self.menu()
        print('your pin has been created successfully')
        self.menu()



    def reset_pin(self):
        old_pin = input('insert old pin: ')
        if old_pin == self.pin:
            create_new_pin = input('set new pin: ')
            self.pin = create_new_pin
            print('your pin has been updated successfully')
        else:
            print('sala garib')
        self.menu()


    def view_balance(self):
        insert_pin = input('insert your current pin: ')
        if insert_pin == self.pin:
            print('your current balance is ',self.balance)
        else:
            print('sale chor nikal yaha se !!!!')
        self.menu()


    def money_withwraval(self):
        insert_pin = input('insert your current pin: ')
        credit_amount = int(input('insert credit amount: '))
        if insert_pin == self.pin and credit_amount < self.balance:
            print(credit_amount,'has been credited')
            self.balance = self.balance - credit_amount
        else:
            print('the amount is bigger then current amount')
        self.menu()




obj = Bank()

