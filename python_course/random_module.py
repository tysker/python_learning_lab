import random

ran_number = random.random() * 10
print(ran_number)

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
pay_the_bill = random.randint(0, len(friends) - 1)
print(friends[pay_the_bill])
print(random.choice(friends))

pales = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
numbers = [1, 2, 3, 4, 5]

merged = [pales, numbers]
print(merged)

print(merged[0])  # ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']
print(merged[1])  # [1, 2, 3, 4, 5]
print(merged[0][2])  # 'Charlie'
print(merged[1][4])  # 5

combined = list(zip(pales, numbers))
print(combined)
