file_name = " ItIsWell (oh my Soul). txt"
word = []
start = 0

for index, each in enumerate(file_name):
    if each == " ":
        word.append(file_name[start:index])
        start = index + 1
        continue
    if each == ".":
        pass

        word.append((file_name[start:]))
        start = index
    if each !=0 and each.isupper():

        word.append((file_name[start:index]))
        start = index
new_word = ""

for index,each in enumerate(word):
    each = each.capitalize()
    new_word += each
    if index != len(word)-1:
        new_word += "_"
print(new_word)
