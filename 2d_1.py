n = int(input("Enter Number : "))

while(n % 2 == 0 and n > 0):
    print(f"{n} is even number")
    break 

while(n % 2 != 0 and n > 0):
    print(f"{n} is odd number")
    break 