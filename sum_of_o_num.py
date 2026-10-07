# Sum of Odd Numbers
# Given n, find the sum of the first n odd numbers.
# Input: 5
# Output: 25
# 1 + 3 + 5 + 7 + 9

n = 5
j = 1
sum = 0
for i in range(1,n+1):
    sum+=j
    j +=2
print(sum)