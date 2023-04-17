gift_price = int(input('Please enter the value of your gift :'))

tax = 0
if gift_price >= 5000 :
    if gift_price >= 5000 and gift_price <= 25000 :
        tax = (100 + (gift_price - 5000) * 0.08)
        print('Value of gift: ', gift_price)
        print('Amount of tax: ', tax)
    elif gift_price >= 25000 and gift_price <= 55000 :
        tax = (1700 + (gift_price - 25000) * 0.10)
        print('Value of gift: ', gift_price)
        print('Amount of tax: ', tax)
    elif gift_price >= 55000 and gift_price <= 200000 :
        tax = (4700 + (gift_price - 55000) * 0.12)
        print('Value of gift: ', gift_price)
        print('Amount of tax: ', tax)
    elif gift_price >= 200000 and gift_price <= 1000000 :
        tax = (22100 + (gift_price - 200000) * 0.15)
        print('Value of gift: ', gift_price)
        print('Amount of tax: ', tax)
    elif gift_price > 1000000 :
        tax = (142100 + (gift_price - 1000000) * 0.17)
        print('Value of gift: ', gift_price)
        print('Amount of tax: ', tax)
else :
    print('gift cannot be taxed')
         