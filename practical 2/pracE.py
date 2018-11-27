finished = False
result = 0
while not finished:
    try:
        num=int(input("Enter the number:"))
        result+=num
    except ValueError:
        print("Please enter a valid integer.")
    print("Valid result is:", result)
