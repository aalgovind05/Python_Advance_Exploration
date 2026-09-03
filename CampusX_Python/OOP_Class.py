class Bank:

    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.menu()

    def get_access(self):
        return self.__balance          #this code will give access to read this variable named self.__balance

    def ser_new(self,new_value):
        self.__balance = new_value
        

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
            self.__balance = deposit
        else:
            print('minimum 5000 INR deposit require to open new account')
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
            print('sale chor nikal yaha se !!!!')
        self.menu()


    def view_balance(self):
        insert_pin = input('insert your current pin: ')
        if insert_pin == self.pin:
            print('your current balance is ',self.__balance)
        else:
            print('sala garib nikal yaha se !!!!')
        self.menu()


    def money_withwraval(self):
        insert_pin = input('insert your current pin: ')
        credit_amount = int(input('insert credit amount: '))
        if insert_pin == self.pin and credit_amount < self.__balance:
            print(credit_amount,'has been credited')
            self.__balance = self.__balance - credit_amount
        else:
            print('the amount is bigger than current amount or pin is incorrect\n please check your pin and withdrawal amount')
        self.menu()




obj = Bank()


#with __balance we have made our balance function as private so no one can access it now but still if you want to access it
# and want to do change on it then you can
#use this "_Class name__function name" kind structure it follow here example = _Bank__balance()

### if ever we want to give access of our variabel than we can use getter and setter methods to give access to others by that upper code

