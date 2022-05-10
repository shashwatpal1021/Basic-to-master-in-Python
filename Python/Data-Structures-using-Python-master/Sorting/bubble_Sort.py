def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

array = [i for i in range(1,11)]
array = array[::-1]
print(array)
bubble_sort(array)
print(array)