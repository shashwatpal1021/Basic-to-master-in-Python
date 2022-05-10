# # Author: OMKAR PATHAk

# from Arrays import Array

# def rotation(rotateBy, myArray):
#     for i in range(0, rotateBy):
#         rotateOne(myArray)
#     return myArray

# def rotateOne(myArray):
#     for i in range(len(myArray) - 1):
#         myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]


# if __name__ == '__main__':
#     myArray = Array(10)
#     for i in range(len(myArray)):
#         myArray.insert(i, i)
#     print('Before Rotation:',myArray)
#     print('After Rotation:',rotation(3, myArray))

#     # OUTPUT:
#     # Before Rotation: 0 1 2 3 4 5 6 7 8 9
#     # After Rotation: 3 4 5 6 7 8 9 0 1 2

import Arrays

# def leftRotation(arr,d):
#     arr[:] = arr[d+1:len(arr)] + arr[0:d+1]
#     return arr



def rightRotation(arr,d):
    arr[:]=arr[len(arr)-d:len(arr)] + arr[0:d]
arr = Arrays.Array(5)
arr.insert(2,4)
arr.insert(3,3)
arr.insert(5,2)
arr.insert(4,0)
arr.insert(1,1)
print(arr)
print(rightRotation(arr,3))