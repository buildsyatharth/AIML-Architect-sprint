## DICTIONARY IN PYTHON
## store data value in key.value pair
## Dictionary is ordered, changeable and does not allow duplicates

## Create a dictionary
info = {
   'name': "AIML Architect",
    "key": "value",
    "dream": "AIML",
    "target": 365,
    "is adult": True,
    "marks": 94.4,
    "subjects": ["Python", "Data Science", "Machine Learning"],
    455 : "Python",
    56.7: "Data Science",
    True : "Machine Learning",
}
print(info)
print(type(info))
print(info["key"])
info["name"] = "my name"
info["surname" ] = "my surname" 

null_dict = {}
null_dict["name"] = "my collage"
print(null_dict)

## Nested Dictionary
student= {
    "name" : "Yatharth",
    "subjects" : {
        "phy" : 97,
        "chem" : 95,
        "maths" : 98
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["phy"])

print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))


pair = list(student.items())
print(pair[0])
print(pair[1])

print(student.get("name2")) # imp to use this method to avoid error

print(student.update({"city" : "Delhi"}))
print(student)

new_dect = {
    "city" : "Delhi",
    "age" : 20
}
print(student.update(new_dect))
print(student)

## SETS IN PYTHON
## Set is the collection of unordered item each element in the set must be unique and immutable

#duplicate values are not allowed in set
collection = {1, 2, 3, 4, "hello", "world", "world", 6, 4,}
print(collection)
print(type(collection))
print(len(collection))

collection1 = {}# empty dict
collection1 = set() # empty set
print(type(collection1))

collection1 = set()
collection1.add(1)
collection1.add("hello")
collection1.add(3.14)
collection1.add("world")
collection1.add((1, 2, 3))
print(collection1)

### collection1.clear()
collection1.remove("hello")
print(collection1)

print(len(collection1))

collection2 = {"hello", "world", "python", "programming"}

print(collection2.pop())# randomly value pop
print(collection2.pop())# randomly value pop

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # union of two sets
print(set1.intersection(set2)) # intersection of two sets




