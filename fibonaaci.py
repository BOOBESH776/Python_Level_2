# Fibonacci Sum
# Given n, find the sum of the first n Fibonacci numbers.
# Input: 6
# Fibonacci: 0 1 1 2 3 5
# Output: 12

n = 6
a=0
b=1
sum = 1
print(a)
print(b)
for i in range(1,n-1):
    c = a+b
    print(c)
    sum+=c
    a=b
    b=c
print("Sum of :",sum)