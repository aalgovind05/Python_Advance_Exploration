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

        print('your pin has been created successfully: ')
        self.menu()




obj = Bank()

