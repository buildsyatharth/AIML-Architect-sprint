# WHILE PRACTICE QUESTION

#1
no = 10
while no <= 15:
    print(no, end=" ")
    no += 1

#2
i = 1
while i <= 5:
    print(i ** 3, end=" ")
    i += 1

#3
i2 = 1
while i2 <= 10:
    if i2 %2 != 0:
        print(i2, end=" ")
    i2 += 1

#4
p = 1
n = 1
while n <= 5:
    p *= n
    n += 1
print(p)

#5
s = input("Enter your sentance : ")
words = s.split()
for word in words:
    i = len(word) - 1
    while i >= 0:
        print(word[i], end= " ")
        i -= 1
    print(end= " ")

#6
word = input("Enter a word to check : ")
vowels = "aeiou"
count = 0
index = 0

while index < len(word):
    if word[index].lower() not in vowels and word[index].isalpha():
        count +=1
    index += 1
print(f"No. of consonents : ", count )

#7
multiple = 3
count = 1

while count <= 5:
    print(multiple, end= " ")
    multiple += 3
    count += 1
#OR
a = 1
b = 3
while a <= 5:
    mu = a*b
    print(mu,)
    a += 1

#8
i = 1
a = int(input("Enter your no : "))
b = int(input("Enter the power of exponent : "))
result = a
while i < b:
    result = result * a
    i += 1
print("Answer :", result)

#9
num = int(input("Enter a no. to check = "))
i1 = 1
is_perfect_square = False

while i1 * i1 <= num:
    if i1 * i1 == num:
        is_perfect_square = True
        break
    i1 += 1

if is_perfect_square:
    print(f"{num} is a perfect square")

else:
    print(f"{num} is not a perfect square")

#10
string = input("Enter a string : ")
char_to_count = input("Enter a character to count : ")
count = 0
index = 0 

while index < len(string):
    if string[index] == char_to_count:
        count += 1
    index += 1
print(f"{char_to_count} + {count}")

# Quick script to calculate Percentage/Cutoff logic for counseling

def check_admission_eligibility(my_score, cutoff_score):
    if my_score >= cutoff_score:
        return "Eligible for Counseling! 🎯"
    else:
        return "Explore other options/rounds. 🏗️"

# Example test
print(check_admission_eligibility(85, 80))

# Evaluating campus visits & course structures

colleges = {
    "SAGE": {"infrastructure": 8, "aiml_curriculum": 9, "distance": 7},
    "LNCT": {"infrastructure": 7, "aiml_curriculum": 8, "distance": 9},
    "ORIENTAL": {"infrastructure": 7, "aiml_curriculum": 7, "distance": 8}
}

def evaluate_campus(name, scores):
    avg_score = sum(scores.values()) / len(scores)
    return f"College: {name} | Architecture Score: {avg_score:.2f}/10"

print("--- University Comparison Report ---")
for name, scores in colleges.items():
    print(evaluate_campus(name, scores))


# FOR LOOP QUESTION 

#1
for i in range(1, 6):
    print(i, end=" ")

#2
for i in range(1, 6,):
    print( i ** 2,)

#3
for i in range(2, 11, 2):
    print(i)

#OR

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#4
total = 0
for i in range(1,11):
    total += i
print(f'Sum is {total}:')

#5
word = input("Enter your word : ")
for i in range(len(word) - 1, -1 ,-1):
    print(word[i], end=" ")

#6
vovels1 = 'aeiou'
L = input("Enter your word : ")
count = 0
# vovels1 = 'aeiou'

for char in L:
    if char in vovels1:
        count +=1

print(f'Total vowels in {L} is {count}')

# 7
# Print Fibonacci Sequance up to 10 Terms 
a = 0
b = 1
# c = a+b
print(a, b , end= " ")

for _ in range(8):
    next_term = a + b
    print(next_term, end= "  ")
    a,b = b, next_term

#8
n = 5
factorial = 1

for i3 in range(1, n+1):
    factorial *= i3
print(f"Factorial of {n} is {factorial}")

#9
num = 7
is_prime = True
for i4 in range(2, int(num ** 0.5)+1):
    if num  % i4== 0:
        is_prime = False
        break

if is_prime and num > 1:
    print(num, "is a prime number")

else:
    print(num,"is not a prime number")

##10
word = "programming"
char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(char + ":", count )