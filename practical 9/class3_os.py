import  os
import shutil
print(os.getcwd())

target_path = "/Users/xuanq_000/Desktop/CP1404/week9/"
os.chdir(target_path)
print(os.getcwd())
print(os.listdir("."))

for name, dirs, files in os.walk("."):
    print(name)

TARGET_PATH ="/Users/xuanq_000/Desktop/CP1404/week9/"
for each in os.listdir("."):
    #print("{} is file?.{} is dir? {]".format(each,os.path.isfile(each),os.path.isdir(each)))
    if os.path.isfile(each):
        slipt_data = each.split(".")
        if slipt_data[1] == "py":
            print(slipt_data[0])
            source = os.path.join(os.getcwd(),each)
            target = os.path.join(TARGET_PATH,each)# join filename to path with separator

            shutil.copyfile(source,target)