import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
rand = random.randint(0, len(friends) - 1)
print(friends[rand])
print(random.choice(friends))