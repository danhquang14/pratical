print(' Electricity bill estimator')
a= int(input ('cents per kWh:'))
b= float(input("daily use in kWh:"))
c=int(input('number of billing days:'))
total=a*b*c/100
print('Estimated bill:',total)