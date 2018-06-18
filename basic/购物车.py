#! -*- coding: utf-8 -*-

money = int(input("Please input your money:"))
products = [['macbook', 12998], ['iphone', 9888], ['xiaomi8', 3688],
            ['hongmi', 988], ['shouhuan', 199]]
index = 0
choosed_number = 0
choosed_products = None
choosed_price = None
confirmed = False

while choosed_number == False:
    print("------this is the products list-----")
    for i in products:
        print("%s:%s" % (i[0], i[1]))
    print("------end-----")

    choosed_products = input("please choose your product which you want:")

    for p in products:
        if p.count(choosed_products) != 0:
            choosed_number = True
            choosed_price = p[1]
            print("you have choose %s, the price is %s" % (p[0], p[1]))
            break

    if choosed_number == False:
        print("\n \n \nYou have choosed the wrong product!!!")

# print(choosed_products, type(choosed_products))
# print(choosed_price, type(choosed_price))

while confirmed == False:
    feedback = input("do you confirm it: yes|no: ")
    if feedback == "yes":
        confirmed = True
        break
    elif feedback == "no":
        print("you give it up!!")
        break
    else:
        print("please confirm it by: yes|no")

if money >= choosed_price:
    money -= choosed_price
    print("you have bought it. still have the money: %s" % (money))
else:
    print("you have no enough money to buy %s" % (choosed_products))
