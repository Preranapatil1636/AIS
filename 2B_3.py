n = 20
list = []

for i in range(n):
    list.append(abs(n))
    n -= 1

for i in range(len(list)):
    print(list[i])