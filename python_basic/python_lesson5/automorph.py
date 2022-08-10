N = int(input("enter a number:"))
for i in range(1, N):
    x = str(i)
    y = str(i**2)
    if x == y[-len(x):]:
        print(i)
