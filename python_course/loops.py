fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

total_exam_score = sum(student_score)
print(total_exam_score)

# sum
sum = 0
for score in student_score:
    sum += score

print(sum)

# max
print(max(student_score))

max = 0
for score in student_score:
    if score > max:
        max = score

print(max)

# range
for number in range(1, 11):
    print(number)

for number in range(1, 11, 2):
    print(number)

total = 0
for number in range(1, 100):
    total += number
print(total)

# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
