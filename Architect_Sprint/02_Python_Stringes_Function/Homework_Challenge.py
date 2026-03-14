#PRACTICE QUESTION 1
name = input("Enter your name : ")
length = len(name)
print("Length of your name is :",(length))

#PRACTICE QUESTION 2
money = "20$_30$_40$"
print(money.count("$"))

#PRACTICE QUESTION 3
light = input("Enter the colour of light:")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("LOOk")
elif(light == ("green")):
    print("GO")
else:
    (print("Light is broken"))

#PRACTICE QUESTION 4
age = int(input("Enter your age :"))
if(age >= 18):
    print("Your are eligible for Vote")
elif(age < 18):
    print("You are not eligible to vote")
else:
    print("Invalid input :")

#PRACTICE QUESTION 5
marks = int(input("Please enter your makrs :"))
if(marks >= 90):
    print("Grade A ")
elif(marks >= 80):
    print("Grade B ")
elif(marks >= 70):
    print("Grade C ")
elif(marks < 70):
    print("Grade D ")    
else:
    print("Invalid input")

#PRACTICE QUESTION 6
age = int(input("Enter your age :"))

if(age < 18):
    print("Canot drive")
elif(age >= 80):
        print("Cannot drive")
else:
    print("Can drive")

#PRACTICE QUESTION 7
no = int(input("Enter your no :"))
rem = no % 2
if(rem ==0 ):
    print("Even :")
else:
    print("Odd :")

#PRACTICE QUESTION 8

no1 = int(input("Yours First no. :"))
no2 = int(input("Your second no. :"))
no3 = int(input("Your third no. "))
no4 = int(input("Your forth no. "))

if(no1 > no2):
    if(no1 > no3):
        if(no1 > no4):
            print("First no. is Greatest")

if(no2 > no1):
    if(no2 > no3):
        if(no2 > no4):
            print("Second no. is Greatest")

if(no3 > no2):
    if(no3 > no1):
        if(no3 > no4):        
            print("Third no. is Greatest")
        
if(no4 > no2):
    if(no4 > no1):
        if(no4 > no4):        
            print("Forth no. is Greatest")
            


#PRACTICE QUESTION 9
number = int(input("Enter your no. :"))

remm = number % 7

if(remm == 0):
    print("The no. is divisible with 7: ")
else:
    print("The no. is not divisible by 7: ")
