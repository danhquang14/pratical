a="""Program to calculate and display a user's bonus based on sales. 
If sales are under $1,000, the user gets a 10% bonus. 
If sales are $1,000 or over, the bonus is 15%. """
print(a)
sales = float(input("Enter sales: $"))
while sales < 1000:
    if sales < 0:
        print('invalid price')
        break
    else:
        print('u get a 10 % bonus')
        a=0.1
        print('total:', sales * a)
        sales = float(input("Enter sales: $"))
else:
    print('the bonus is 15% ')
    a=0.15
    print('total:', sales * a)
    sales = float(input("Enter sales: $"))