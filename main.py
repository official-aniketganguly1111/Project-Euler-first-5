#Find the smallest number that is divisible with all integers from 1 to 20

#It's the Least Common Multiple; lcm(1,2, ..., 20)
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)

llcm = lcm(11, 12)
for n in range(12, 20):
  llcm = lcm(n, llcm)

print(llcm)
