import random

friends = ["Sagar", "Raju", "Praveen", "Deepak", "Vinod",]

# 1st Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])