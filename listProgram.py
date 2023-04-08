myList = ['STRING', 100, 23,4]
print(len(myList))
myList =['one','two','three']
print(myList[1:])
print(myList)
anotherList = ['four','five']
newList = myList + anotherList
print(newList)
newList[0] = 'ONE ALL CAPS'
print(newList)
newList.append('six')
print(newList)
newList.append('seven')
print(newList)
print(newList.pop())
print(newList)
poppedItem = newList.pop()
print(poppedItem)
print(newList)
print(newList.pop(0))
print(newList)
newList = ['a','e','i','o','u']
numList = [4 ,2,3,4,5,6,]
print(newList.sort())
print(newList)
mySortedList = newList.sort()
print(type(mySortedList))
newList.sort()
mySortedList = newList
print(mySortedList)
print(numList)
numList.reverse()
print(numList)
lst= [0,1,2]
print(lst)
lst = ['a', 'b','c']
print(lst[1:])