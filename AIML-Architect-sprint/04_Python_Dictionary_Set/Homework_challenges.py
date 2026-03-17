#PRACTICE QUESTION 1
dict1 = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "used for eating", "used for studying"],
}

# print(dict1)

#PRACTICE QUESTION 2
list1 = {"python", "java", "c++", "python", "javascript"}
list2 = {"python", "java", "c++", "c"}
u = list1.union(list2)
print(len(u))

#PRACTICE QUESTION 3
dict2 = {}
dict2["Name"] = input("Enter your name: ")
dict2["PHYSICS"] = int(input("Enter your physics marks: "))
dict2["CHEMISTRY"] = int(input("Enter your chemistry marks: "))
dict2["MATHS"] = int(input("Enter your maths marks: "))
print(dict2)

#PRACTICE QUESTION 4
value = {9, "9.0"}
print(value)

value = {
    ("float", 9.0),
    ("int", 9),
}
print(value)