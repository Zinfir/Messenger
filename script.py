list = [1, 2]
while True:
    l = len(list)
    a = list[l - 1]
    b = list[l - 2]
    c = a + b
    if c < 4000000:
        list.append(c)
    else:
        break
sum = 0
for i in list:
    if i % 2 == 0:
        sum += i
print(sum)
