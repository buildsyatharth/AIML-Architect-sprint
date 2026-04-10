##1 Check if a number is even or odd
##2 Print all even numbers from 1 to N
##3 Count number of odd numbers in a list

#1
int1 = int(input("ENTER YOUR NO. :"))
if int1 % 2 == 0:
    print("NO IS EVEN")
else:
    print("NO IS ODD")

#2
int2 = int(input("Enter your no: "))
int3 = 1
while int3 <= int2:
    if int3 % 2 == 0:
        print(int3)
    int3 += 1

#3
list1 = (input("Enter your no list :")).split()
count1 = 0
for a in list1:
    if int(a) % 2 != 0:
        count1 += 1
print(count1)

#Check if sum of digits of a number is even or odd
#Given two numbers, check if their product is even or odd
#Find if a number becomes odd after adding 7

#1
str1 = (input("enter your no :"))
total = 0
for b in str1:
    total = total + int(b)
if total % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")

#2
int4 = int(input("Enter your no :"))
int5 = int(input("Enter your no :"))
prd = int4 * int5
if prd % 2 == 0:
    print(prd, "Product is even")
else:
    print(prd,"Product is odd")

#OR

int7 = int(input("Enter your no :"))
int8 = int(input("Enter your no :"))

if int7 % 2 == 0 or int8 % 2 == 0:
    print("Product is even")
else:
    print("Product is odd")

#3
int6 = int(input("Enter your no :"))
if (int6 + 7) %2 != 0:
    print("No. become odd")
else:
    print("No. is even")

## Without using %, check even/odd
## Check if a number is even using bitwise operator
## Count even numbers in range divisible by 3

#1
int7 = int(input("Enter your no :"))
last_digit = str(int7)[-1]
if last_digit in "02468":
    print("No. is even")
else:
    print("No is odd")

##OR
int8 = int(input("Enter your no. :"))
if int8 - (int8 // 2) * 2 == 0:
    print("EVEN")
else:
    print("ODD")

##2
int9 = int(input("Enter your no. "))
a = 1
found = False
while a <= int9:
    if a % 3 == 0 and a % 2 == 0:
        found = True
        print(a)
    a += 1

if found == False :
    print("No number in range")