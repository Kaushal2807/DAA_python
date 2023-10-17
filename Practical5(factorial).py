# def factorial(n):
#     if n == 1 :
#         return 1 
#     elif n<0:
#         print("Invaild Input")
#     else :
#         return (n*factorial(n-1))
        
# num = int(input("Enter a number:="))
# print(factorial(num))

n=int(input("Enter a number tp find the factorial:-"))
factorial = 1
if n<0:
    print("Invalid input.")
elif n==0:
    print("The factorial of 0 is 1:-")
else:
    for i in range(1,n+1):
        factorial= factorial*i
    print(factorial)