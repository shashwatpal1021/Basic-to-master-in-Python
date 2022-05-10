# def insertion_sort(array):
#     global iterations
#     iterations = 0
#     for i in range(1, len(array)):
#         current_value = array[i]
#         for j in range(i - 1, -1, -1):
#             iterations += 1
#             if array[j] > current_value:
#                 array[j], array[j + 1] = array[j + 1], array[j] # swap
#             else:
#                 array[j + 1] = current_value
#                 break


# # elements are reverse sorted
# array = [i for i in range(1, 20)]
# # reversing the array
# array = array[::-1]
# print(array)

# insertion_sort(array)
# # 20 REVERSE sorted elements need 324 iterations approx = n * n

# print(array)
# print(iterations)


def inserstion_sort(arr):
    for i in range(1,len(arr)):
        current_value = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>current_value:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                arr[j+1]=current_value
                break


arr = [i for i in range(20,0,-1)]
print(arr)
inserstion_sort(arr)
print(arr)