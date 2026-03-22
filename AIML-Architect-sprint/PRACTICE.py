#PRACTICE QUESTION

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