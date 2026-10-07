# 1.Given n, find the sum of the first n even numbers.
# Input: 5
# Output: 30
# 2 + 4 + 6 + 8 + 10
n = 5
j = 2
sum = 0
for i in range(1,n+1):
    sum+=j
    j +=2
print(sum)