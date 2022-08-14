a = str(input("Enter two words:"))
count = a.count(' ')
i = a[::-1]
if count == 1:
    print(i.capitalize())
    i = a[::-1]
else:
    print(input("Please, enter two words using space:"))
