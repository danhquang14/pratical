names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]

full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",

              "Ada Lovelace"]

# TODO: use a list comprehension to create a list of all of the full_names

# in lowercase format

# lowercase_full_names

name=[x.lower()for x in full_names]
print(name)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: use a list comprehension to create a list of integers

# from the above list of strings

# numbers
a=[int(x) for x in almost_numbers]
print(a)

# TODO: use a list comprehension to create a list of only the numbers that are

# greater than 9 from the numbers (not strings) you just create
b=[int(x)for x in almost_numbers if int(x)>9]
print(b)