n = int(input("Enter numbers from 3 to 9:"))

if n in range(3, 10):
    rows = n
    for i in range(1, rows + 1):
        for j in range(1, i - 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
else:
    print("finish")