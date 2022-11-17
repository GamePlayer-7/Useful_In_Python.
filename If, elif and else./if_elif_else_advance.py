price_per_head = 50
quantity = 5
amount = price_per_head * quantity

if amount > 100:
    if amount > 500:
        print("Amount is greater than 500")
    else:
        if amount < 500 and amount > 400:
            print("Amount is between 400 and 500")
        elif amount < 500 and amount > 300:
            print("Amount is between 300 and 500")
        else:
            print("Amount is between 200 and 500")
elif amount == 100:
    print("Amount is 100")
else:
    print("Amount is less than 100")

#Below is the Output :

Amount is between 200 and 500
