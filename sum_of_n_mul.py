# Sum of Multiples

# Given n, find the sum of the first 10 multiples of n.
# Input: 5
# Output: 275

n=5
sum=0
for i in range(1,11):
    res = i*n
    sum = sum + res
print(sum)