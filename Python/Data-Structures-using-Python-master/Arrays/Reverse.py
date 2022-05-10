# Author: OMKAR PATHAK

# import Arrays

# def  reversingAnArray(start, end, myArray):
#     while(start < end):
#         myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
#         start += 1
#         end -= 1

# if __name__ == '__main__':
#     myArray = Arrays.Array(10)
#     myArray.insert(2, 2)
#     myArray.insert(1, 3)
#     myArray.insert(3, 1)
#     print('Array before Reversing:',myArray)
#     reversingAnArray(0, len(myArray), myArray)
#     print('Array after Reversing:',myArray)


import Arrays

def reverse(arr):
    arr [:] =arr[::-1]
    return arr


arr = Arrays.Array(10)
arr.insert(2, 2)
arr.insert(1, 3)
arr.insert(3, 1)
print(arr)
print(reverse(arr))