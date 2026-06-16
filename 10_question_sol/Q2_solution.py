age = int(input('what is your age :'))
day = 'friday'
price = 12 if age >= 18 else 8

if day == "wednesday":
    price-=2
    # price == price - 2 (this one and up onr price -= 2 are work same
    #but always prefer price -= 2)

print("ticket price for you is $",price)