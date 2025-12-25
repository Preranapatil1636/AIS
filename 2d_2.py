# PATTERNS ->

n = int(input("Enter number : "))

i = 1
while(i <= n):
    print("* " * i)
    i += 1

# for i in range(1,n+1):
#     print("*" * i)

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             print("# ",end="")    
#         else :
#             print("* ",end="")
#     print("")

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if ((i == 1 or j == 1) or (i == n or j == n)):
#             print("* ",end="")
#         else :
#             print("  ",end="")
#     print("")