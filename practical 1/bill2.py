print("Electricity bill estimate 2.0")
a=int(input("which tariff? 11 or 31"))
print(a)
while True:
    if a==11:
        break
    elif a==31:
        break
    else:
        print("invalid number")
        a = int(input("which tariff? 11 or 31"))
b= float(input("daily use in kWh:"))
c=int(input('number of billing days:'))
total=a*b*c/100
print('Estimated bill:',total)