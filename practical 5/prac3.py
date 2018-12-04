a=str(input("please enter the text:"))
print("text:"+a)
b=a.split()
c=dict()
lenght_text = []

for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
d=sorted(c)
for each in b:
    lenght = len(each)
    lenght_text.append(lenght)
max_lenght = max(lenght_text)
for each in d :
    print("{:{}} : {}".format(each,max_lenght, c[each]))