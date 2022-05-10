def partition(array, low, high):
    i = low - 1            # index of smaller element
    pivot = array[high]    # pivot 
    
    for j in range(low, high):
        # If current element is smaller than the pivot
        
        if array[j] < pivot:
        # increment index of smaller element
        
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place 
        temp = partition(array, low, high)
        
        # Separately sort elements before
        # partition and after partition 
        quick_sort(array, low, temp - 1)
        quick_sort(array, temp + 1, high)

# elements are reverse sorted
array = [i for i in range(1, 20)]
# reversing the array
array = array[::-1]

print(array)
# 20 REVERSE sorted elements need 324 iterations approx = n * n
quick_sort(array, 0, len(array) - 1)
print(array)

def quick_sort(arr):
    global low
    low = 0
    global high
    high = len(arr)

rem= 0
while(len(n)>1):
    
    for i in n:
        rem += int(n[i])
        n=rem
        print(n)
    print(n)



