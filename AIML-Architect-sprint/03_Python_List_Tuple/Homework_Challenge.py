#PRACTICE QUESTION 1
name = str(input("Enter your first favorite movie name: "))
name2 = str(input("Enter your second favorite movie name: "))
name3 = str(input("Enter your third favorite movie name: "))
movies = [name, name2, name3]
print(movies)
print(type(movies))
print(movies[0])
print(movies[1])
print(movies[2])

#PRACTICE QUESTION 2
# WAP to check if a list contain a palindrome of element
# Palidrome is a word which is same when read from left to right and right to left

list0 = int(input(" ENTER YOUR NUMBER: "))
list1 = int(input(" ENTER YOUR NUMBER: "))
list2 = int(input(" ENTER YOUR NUMBER: "))

lista = [list0, list1, list2]

copy_lista = lista.copy()
copy_lista.reverse()

if copy_lista == lista:
    print("The list contain a palindrome of element")
else:
    print("The list does not contain a palindrome of element")

# PRACTICE QUESTION 3
GRADE = ("C", "D", "A", "A", "B", "B", "A")
print(GRADE.count("A"))

# PRACTICE QUESTION 4
listz = ["C", "D", "A", "A", "B", "B", "A"]
listz.sort()
print(listz)