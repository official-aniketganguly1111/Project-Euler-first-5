#Only the even fibonacci numbers
i = 0
j = 1
list1 = list()
sum2 = 0
for k in range(10):
    sum1 = i + j
    i = j
    j = sum1
    list1.append(sum1)

print(list1)

for m in list1:
    if m < 10:
        if m % 2 == 0:
            sum2 = sum2 + m

print(sum2)
