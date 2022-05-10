def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    result = []
    i,j = 0, 0
    while i<len(left) or j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

arr = [i for i in range(20,0,-1)]
print(arr)
print(merge_sort(arr))

