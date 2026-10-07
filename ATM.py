# Give the user a maximum of 3 attempts to enter a password. Use a while loop.
# Correct password → "Login Successful"
# Three wrong attempts → "Account Locked"
# After each wrong attempt, display the remaining attempts.


# pw = 123
# i=3
# n=int(input("Enter Password"))
# while True:
#     if n==pw:
#         print("Login Succcessfull")
#         break
#     else:
#         i = i - 1
#         if i==0:
#             print("Account Locked")
#             break
#         else:
#             print("You have ", i, "attempt")
#             n = int(input("Enter Password"))

# Using For Loop
pw = 123
i=3
a = 3
n=int(input("Enter Password"))
for i in range(1,i+1):
    if n==pw:
        print("Login Successful")
        break
    else:
        a=a-1
        if a == 0:
            print("Account Locked")
            break
        else:
            print("Attempt :",a)
            n=int(input("Enter Password"))