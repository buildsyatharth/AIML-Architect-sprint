#PRACTICE QUESTION 1
i = 1
while i <= 100:
    print(i)
    i+= 1

#PRACTICE QUESTION 2
i = 100
while i >= 1:
    print(i)
    i -= 1

#PRACTICE QUESTION 3
n = int(input("Enter a number: "))
i1 = 1
while i1 <= 10:
    print(n*i1)
    i1 += 1

#PRACTICE QUESTION 4
#traverse a list using while loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i2 = 0
while i2 < len(nums):
    print(nums[i2])
    i2 += 1
 
heroes = ["Superman", "Batman", "Wonder"]

idx = 0 
while idx < len(heroes):
    print(heroes[idx])
    idx += 1
 
#PRACTICE QUESTION 5
inn = int(input("Enter a number: "))

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

i3 = 0 # initialization
while i3 < len(tup):
    if(tup[i3] == inn):
        print("Found", i3)
        break   
    else:
        print("finding", tup[i3])
    i3 += 1

#PRACTICE QUESTION 6
i4 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in i4:
    print(val)

#PRACTICE QUESTION 7
for i in range(1 , 101, 1):
    print(i)

#PRACTICE QUESTION 8
for i in range(1 , 101, 1):
    print(i)

#PRACTICE QUESTION 9
for i in range(100, 0, -1):
    print(i)

#PRACTICE QUESTION 10
nu = int(input("Enter a number: "))
for i in range(1, 11):
    print(nu*i)

# PRACTICE QUESTION 11

n = int(input("Enter a number: "))

sum = 0
for i in range(1, n+1):
    sum += i

print("Sum", sum,)

#PRACTICE QUESTION 12

n1 = int(input("Enter a number: "))
fact = 1
iq = 1
while iq <= n1:
    fact *= iq
    iq += 1

print("Factorial", fact)

n2 = int(input("Enter a number: "))
fact = 1

for i in range(1, n2+1):
    fact *= i

print("Factorial", fact)