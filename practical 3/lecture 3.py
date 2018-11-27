while True:
    try:
        a=int(input("enter your age:"))
        if a%2==0:
            print("the number is an even")
        else:
            print("the number is an odd")
        break;
    except ValueError:
        print("Enter a valid number:")
