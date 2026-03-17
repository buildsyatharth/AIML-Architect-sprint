###LOOPS IN PYTHON
###1. While loop 2. For loop

count = 1 #iterator moving in loop is iteration
while count <= 5:
    print("Hello")
    count += 1

i1 = 1
while i1 <= 5:
    print("helloe", i1)
    i1 += 1

# print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# print("Done")   

##Break and continue statement 

i3 = 1
while i3 <= 5:
    print(i3)
    if(i3 == 3):
        break
    i3 += 1
print("Done")


n = int(input("Enter a number: "))
i4 = 1
while i4 <= n:
    if (i4 %2 == 0):
        i4 += 1
        continue #skips
    print(i4)
    i4 += 1


#FOR LOOP

list = [1, 2, 3, 4, 5]
veg = ["tomato", "potato", "onion", "carrot"]

for val in list:
    print(val)

for val in veg:
    print(val)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for val in tup:
    print(val)

str = "Hello"
for val in str:
     print(val)
else: 
    print("Loop is over")# in specific case when break is used


#RANGE FUNCTION
# start from 0 to n-1

seq = range(10)
for i in range(10):
    print(i)
    
# range (start ? Optional default 0, stop, step ? Optional default 1)
for i in range(1, 100, 2):
        print(i, "odd numbers")
for i in range(2, 100, 2):
        print(i, "even numbers")

#PASS statement
for i in range(5):
     pass #placeholder for future code, it does nothing
     if i > 5:
        pass
     
     print("some useful code")