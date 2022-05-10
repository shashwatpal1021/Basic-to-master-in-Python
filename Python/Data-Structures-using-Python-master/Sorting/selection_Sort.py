def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        if min_index != i:
            arr[i],arr[min_index] = arr[min_index],arr[i]

arr = [i for i in range(21,0,-1)]
print(arr)
selectionSort(arr)
print(arr)