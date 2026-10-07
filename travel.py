# Distance Traveled
# A car travels 10 km in the first hour, 20 km in the second hour, 30 km in the third hour, and so on.
# Given n hours, calculate the total distance.
# Input: 5
# Output: 150
n = 5
km = 0
sum = 0
for i in range(1,n+1):
    km+=10
    sum+=km
    print("km :",km)
print("sum :",sum)
