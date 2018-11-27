numbers=[]
for i  in range(5):
    a=int(input("Enter the number:"))
    numbers.append(a)
print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[-1]))
print("the smallest number is {}".format(min(numbers)))
print("the largest number is {}".format(max(numbers)))
print("the average number is {}".format(sum(numbers)/5))