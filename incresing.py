# Increasing Payment
# A person makes payments of ₹100, ₹200, ₹300, ... for n months.
# Find the total amount paid.
# Input: 6
# Output: 2100

n = 6
am = 100
sum = 0
for i in range(1,n+1):
    print(am)
    sum+=am
    am+=100
print("Sum of :",sum)