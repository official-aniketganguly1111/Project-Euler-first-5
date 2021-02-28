#Largest Prime Factor of an Numbers
import math

n = int(input("Enter an Number\n"))
list1 = list()
#Loop to store the factors in a list
for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i) == 0:
        list1.append(i)
        while i != int(math.sqrt(n)):
            list1.append(int(n / i))
            break
#Loop to find the largest prime factor
for k in list1:
    for j in range(2, k):
        if k % j == 0:
            break
    else:
        prev = k


print(prev)
