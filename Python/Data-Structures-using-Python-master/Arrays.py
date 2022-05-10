class Array():
    def __init__(self, sizeofArray, arrayType = int):
        self.sizeofArray = len(list(map(arrayType,range(sizeofArray))))
        self.arrayItems = [arrayType(0)]*sizeofArray

    def __str__(self):
        return " ".join([str(i) for i in self.arrayItems])

    def search(self, keyToSearch):
        for i in range(self.sizeofArray):
            if(self.arrayItems[i] == keyToSearch):
                return i

        return -1

    def insert(self, keyToInsert, position):
        if (self.sizeofArray > position):
            for i in range(self.sizeofArray - 2, position - 1, -1):
                self.arrayItems[i+1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array of size is : ',self.sizeofArray)

    def delete(self,keyToDelete, position):
        if (self.sizeofArray > position):
            for i in range(position, self.sizeofArray - 1):
                self.arrayItems[i] = self.arrayItems[i+1]

            else:
                print('Array size is : ',self.sizeofArray)

a = Array(10,int)
a.insert(1,2)
a.insert(5,3)
a.insert(3,4)
print(a)
a.delete(5,3)
print(a)
index = a.search(3)
print('element found at index: ',index)

