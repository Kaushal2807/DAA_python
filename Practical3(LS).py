def linearSearch(l,n,x):
    for i in range(0,n):
        if l[i]==x:
            return i
    return -1

n = int(input("Enter size of array:="))
l = []
print("Enter Elements:=")
for i in range(n):
    a=int(input())
    l.append(a)
print(l)
x = int(input("Enter element to Search:="))
result = linearSearch(l,n,x)
if result == -1:
    print("Element is not found")
else:
    print("Element found at index: ",result)