#Multiples of 3 and 5
i = 1
sum1 = 0
#looping statement
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum1 = sum1 + i

print(sum1)

