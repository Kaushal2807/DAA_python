# Quick Sort

# def quickSort(a):
#     if len(a)<= 1:
#         return a
#     else :
#         pivot = a.pop()

#     greater = []
#     lower = []

#     for i in a :
#         if i > pivot:
#             greater.append(i)

#         else:
#             lower.append(i)
#     return quickSort(lower)+[pivot]+quickSort(greater)

# l=[98,55,65,25,11,0]
# print(quickSort(l))

def quickSort(arr,n):
    if n<= 1:
        return arr
    else :
        pivot = arr.pop()

    greater = []
    lower = []

    for i in arr :
        if i > pivot:
            greater.append(i)

        else:
            lower.append(i)
    return quickSort(lower,len(lower))+[pivot]+quickSort(greater,len(greater))

n = int(input("Enter size of array :="))
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
    
print(quickSort(arr,n))

