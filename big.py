# Given three numbers, find the largest number and calculate how much larger it is than the smallest number.
# Input: 12 30 18
# Output: 18
a = 12
b = 30
c = 18
if a>b and a>c:
    print("a")
    if a>b:
        print(a-b)
    else:
        print(a-c)
elif b>a and b>c:
    print("b")
    if b>a:
        print(b-a)
    else:
        print(b-c)
elif c>a and c>b:
    print("c")
    if c>a:
        print(c-a)
    else:
        print(c-b)

