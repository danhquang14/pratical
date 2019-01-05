"""
with open("data.csv","r")as my_file:
    for each in my_file :
        print(each)
"""


import csv

file_obj = open("data.csv","r")
csv_obj = csv.reader(file_obj)
for row in csv_obj:
    print(row)

file_obj.close()

print("*"* 100)

counter = 0
with open("data.csv","r") as file_obj:
    csv_obj = csv.reader(file_obj)
    for row in csv_obj:
        counter +=1
        print("counter = {}".format(counter))

"""
file_obj = open("data.csv","r")
for row in csv_obj:
    print(row)
    
file_obj.close()
"""

counter = 0
counter_list = []
csv_out = open("out.csv","w")
csv_wrapper = csv.writer(csv_out)
with open("data.csv","r") as file_obj:
    csv_obj = csv.reader(file_obj)
    for row in csv_obj:
        counter +=1
        print("counter = {}".format(counter))
        counter_list.append("counter = {}".format(counter))
    csv_wrapper.writerow(counter_list)# goes hand in hand with csv.writer

csv_out.close()