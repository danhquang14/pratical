"""
Download the csv fi,e from week 9 and save it as sales.csv in your working directory

write a program with the following requirment:
1. A class called House with 3 attributes (br , sqft, price)
2. use with and csv.reader to read the sales.csv
3.process the data, must make use of object created from House and print out:
  the average price per square for 3 bedroom.

"""
"""
class House:
    def __init__(self,bedroom,square,price):
        self.bedroom = bedroom
        self.square = square
        self.price = price

    def __str__(self):
        return "the average {}$ per {} square for {} bedroom  ".format(self.price,self.square,self.bedroom)



import csv

with open("sales.csv","r") as file_open:
    csv_file = csv.reader(file_open)
    price_list = []
    square_list = []
    for row in csv_file:
        #data = House(row[4],row[6],row[9])
        #print("the average {}$ per {} square for {} bedroom  ".format(row[9],row[6],row[4]))

        if row[4] == 3:
            price_list.append(row[9])
            square_list.append(row[6])

    print(price_list,square_list)

    #average = sum(price_list)/sum(square_list)
    #print("the average {} per square for 3 bedroom".format(average))

"""
import csv
class House:
    def __init__(self,bedroom,square,price):
        self.bedroom = bedroom
        self.square =square
        self.price =price

    def __str__(self):
        return "the average {}$ per {} square for {} bedroom  ".format(self.price, self.square, self.bedroom)

def process_file(filename):
    data =[]
    with open(filename,"r")as file_obj:
        csv_pointer = csv.reader(file_obj)
        counter = 0
        for row in csv_pointer:
            counter +=1
            if counter ==1:
                continue
            house_obj = House(row[4],row[6],row[9])
            data.append(house_obj)


    return data

def get_average(house,number_of_bed):
    total_price =0
    total_square =0
    for each in house:
        if int(each.bedroom) == number_of_bed:
            total_price += int(each.price)
            total_square += int(each.square)

    print("the average price for {} bedder is {}".format(number_of_bed,total_price/total_square))
def main():
    FILENAME = "sales.csv"
    data = process_file(FILENAME)
    get_average(data,3)

main()