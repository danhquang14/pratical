a=str(input("please enter your name?"))
print("Enter name:",a)
print('''(H)ello
(G)oodbye
(Q)uit''')
b=str(input('Choose now!:'))
while True:
    if b.upper()=='H':
        print('Hello',a)
        break
    elif b.upper()=='G':
        print('Goodbye',a)
        break
    elif b.upper()=='Q':
        print('Finished')
        break
    else:
        print("please try again!")
        b = str(input('Choose now!:'))


