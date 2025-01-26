import random

def nums():
    num = [1, 5, 8, 9, 11, 10]

    return random.choice(num)

def calculate(nums):

    if sum(nums) == 21 and len(nums) == 2:
        return 0
    
    if 11 in nums and sum(nums) > 21:
        nums.remove(11)
        nums.append(1)
    
    return sum(nums)

# print(num)

# if 11 in num:
#     print("Found 11")
#     num.remove(11)
#     # num.append(1)
#     print(num)
# else:
#     print("Not found 11")

my_num = []

for _ in range(2):
    my_num.append(nums())

print(my_num)

print(f"Sum of numbers is: {calculate(my_num)}" )