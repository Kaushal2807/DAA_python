def BubbleSort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binarySearch (arr, low, high, x):
    if low <= high:
        mid =(high + low) // 2

        if x < arr[mid]:
            return binarySearch(arr, low, mid - 1, x)

        elif x > arr[mid]:
            return binarySearch(arr, mid + 1, high, x)

        else:
            return mid
        
    else:
        return -1
    
n= int(input("Enter size of array := "))
arr=[]
print("Enter Elements := ")
for i in range(n):
    a = int(input())
    arr.append(a)
# print(arr)

BubbleSort(arr)

print("Sorted Array :=")
for i in range (len(arr)):
    print(arr[i], end=" ")

x = int(input("\nEnter element to Search := "))
result = binarySearch(arr, 0, len(arr), x)

if result == -1:
    print("Element not found")
else:
    print("Element found at index: ",result)