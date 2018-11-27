import random
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05  
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = float(input('Enter the price in range from $1 to $100'))
while INITIAL_PRICE>1 or INITIAL_PRICE<100:
	price = INITIAL_PRICE
	print("starting price is :${:,.2f}".format(price))
	count = 0
	while price >= MIN_PRICE and price <= MAX_PRICE:
   	 	price_change = 0
   	 	if random.randint(1, 2) ==1:
   	 		price_change = random.uniform(0, MAX_INCREASE)
   	 	else:
   	 		price_change = random.uniform(-MAX_DECREASE, 0)
   	 	count += 1
   	 	price *= (1 + price_change)
   	 	print("on day {} price is ${:,.2f}".format(count,price))
else:
	print("Sorry, please enter again in range $1 to $100.")