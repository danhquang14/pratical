a=int(input('Number of items:'))
list=[]
total=0
while a<0:
    print('please try again')
    a = int(input('Number of items:'))
for i in range(a):
    b=float(input('Price of item:'))
    list.append(b)
    total=sum(list)
if total>100:
    p=0.1
    total=p*0.1
    print(total)
else:
    print(total)


