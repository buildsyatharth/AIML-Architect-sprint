# escape squance character are special charatr for formating
 
str = "this is a strimg. \nwe are creating in python"
print(str)
#guve a space of tab between two sentance
str0 = "this is a strimg. \twe are creating in python"
print(str0)

#OPERATION 

# Concatention 
str1 = "my world"
str2 = "college"
strF = str1 + str2
print(strF)

#Length of str
len1 = len(str1)
print(len1)
len2 = len(str2)
print(len2)
final_str = str1 + " "+ str2
print(final_str)
print(len(final_str))

#INDEXING 
str3 = "college"
ch = str3[4]
print(ch)

#SLICING (IMP ML)
str4 = "good college"#start index is ever included
print(str4[5:12])
print(str4[2:len(str4)])# 2 to end tak jaiga
print(str4[2:])# 2 to end tak jaiga[2,end]
print(str4[ :7])#start se 7 tak [0,7]

#negative slicing
str5 = "My Dream"
print(str5[-5:-1])
print(str5[-7:-1])
#Strimg Function
str6 = "i am studying python from Apna college"
print(str6.endswith("ege"))
print(str6.endswith("spp"))
print(str6.endswith("tt"))

str6 = str6.capitalize()#to save the modified string in old string
print(str6.capitalize())
print(str6.replace("o", "1"))#to replace a letter
print(str6.replace("t", "5"))
print(str6.replace("studying" , "love"))
print(str6.find("f"))
print(str6.find("from"))
print(str6.find("z"))
print(str6.count("u"))

#Conditional Statement (if)(elif)(else)
age1 = 19
if(age1 >= 18):
    print("Can vote and apply for DL")
    print("Cam drive and vote")
age1 = 20#same task as above
if(True):
    print("Can write and vote in election")

#elif if first is not true then this 

light = input("Enter the colour of light:")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):# gap is known is indentation (the space we gave of foul times)
    print("LOOk")
elif(light == ("green")):
    print("GO")
else:
    (print("Light is broken"))

#NESTING

age = int(input("Enter your age :"))

if(age >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("Can drive")









      





















