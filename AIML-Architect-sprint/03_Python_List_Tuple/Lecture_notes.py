#LIST IN PYTHON
marks = [94.4, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

#STRINGS ARE IMMUTABLE IN PYTHON 
#LISTS ARE MUTABLE IN PYTHON

str = ["hello"]
print(str[0])
str[0] = "Argun"
print(str)

#LIST SLICING
marks1 = [66, 77, 44, 23, 11, 22, 44, 55]
print(marks1[1:3])
print(marks1[2:])
print(marks1[:9])
print(marks1[-1:-4])

#LIST METHODS(appened, sort, reverse, insert)
list = [2, 1, 3]
list.append(4)#to add something in end like an element or an no.
print(list)
list.sort()# sort method directly dont return anything(assending)
print(list)
list.sort(reverse =True)#desending
print(list)

list1 = ["banana", "Litchi", "apple"]
list1.append("Bro code")
# list1.sort()
list1.sort(reverse=True)
print(list1)

list2 = ["a", "d", "g", "f", "c", "b"]
list2.reverse()
print(list2)
list2.append("z")
print(list2)
list2.sort(reverse=True)
print(list2)
list2.sort()
print(list2)

list3 = [0, 1, 2, 3, 4, 5]
list3.insert(2, "Apple")#list.insert(imdex postion , element postion)
print(list3)
list3.insert(0 , 6)
print(list3)

list4 = [2,1,3,1]
list4.pop(1)
print(list4)
list4.count(1)
print(list4)

#TUPLE IN PYTHON
#Tuple are built in data type that let us create immutable sequences of data.
#Tuples are similar to lists but they cannot be modified after they are created.

tup = (1, 2, 3, 4, 5)
print(type(tup))
print(tup[0])
print(tup[3])

tup1a = (1,) #if we remove comma the value (1) become integer and not tuple
print(tup1a)
print(type(tup1a))

tupb = (1)
print(tupb)
print(type(tupb))

tupc = (1.6) 
print(tupc)
print(type(tupc))

tupd = ("integer") 
print(tupd)
print(type(tupd))

tupe = (1, 2, 3, 4,)#Slicing in tuple
print(tupe[1:3])

#TUPLE METHODS
tup1 = (1, 2, 3, 2, 2)
tup.index(2)
print(tup1.index(2))
tup1.count(2)
print(tup1.count(2))