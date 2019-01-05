import os, shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())
os.chdir('FilesToSort')
os.mkdir('xlsx')
for filename in os.listdir('.'):
    if ".xlsx" in filename:
        shutil.move(filename, 'xlsx')
os.mkdir('xls')
for filename in os.listdir('.'):
    if ".xls" in filename:
        shutil.move(filename, 'xls')
os.mkdir('txt')
for filename in os.listdir('.'):
    if ".txt" in filename:
        shutil.move(filename, 'txt')
os.mkdir('png')
for filename in os.listdir('.'):
    if "png" in filename:
        shutil.move(filename, 'png')
os.mkdir('jpg')
for filename in os.listdir('.'):
    if ".jpg" in filename:
        shutil.move(filename, 'jpg')
os.mkdir('gif')
for filename in os.listdir('.'):
    if ".gif" in filename:
        shutil.move(filename, 'gif')
os.mkdir('docx')
for filename in os.listdir('.'):
    if ".docx" in filename:
        shutil.move(filename, 'docx')
os.mkdir('doc')
for filename in os.listdir('.'):
    if ".doc" in filename:
        shutil.move(filename, 'doc')
