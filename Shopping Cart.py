
############ SHOPPING CART FOOD ################# 


foods =  [] 
prices = []
total = 0 

while True : 
    food = input("Enter your food (q to quit ) : ")
    if food.lower() == "q" : 
     break
    else :
        price = float(input(f"Enter your price of {food} $"))
        prices.append(price)
        foods.append(food)

print ("--------------->>>>> Your Cart <<<<<---------------")
    
for food in foods :
    print (food , end = " ")


for price in prices : 
    total += price 

print ()
print (f"Your total is  : {total} $")    













