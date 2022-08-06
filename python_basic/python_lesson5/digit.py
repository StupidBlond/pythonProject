n = input("enter a number:")
x = 0
for i in range(0, len(n)):
    for k in range(i+1, len(n)):
        if n[i] == n[k]:
            x += 1
if x > 0:
    print('yes')
else:
    print('no')

