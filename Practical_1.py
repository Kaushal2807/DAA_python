def insertionSort(array):
    for i in range (0,len(array)):
        key=array[i]

        j=i-1

        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key

data = [5,4,6,32,89]
insertionSort(data)
print(data)



def selectionSort(array,size):
    for i in range (size):
        min_index = i

        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        (array[i],array[min_index]) = (array[min_index],array[i])

data1 = [7,9,2,3,1]
size=len(data1)
selectionSort(data1,size)
print(data1)



def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data2=[25,2,5,36,6]
bubbleSort(data2)
print(data2)