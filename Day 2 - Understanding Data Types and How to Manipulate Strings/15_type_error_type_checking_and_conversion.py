# print("Number of letters in your name: ", len(input("Enter your name: ")))

user_name = input("Enter your name: ")

length_of_user_name = len(user_name)

# print(type(length_of_user_name))
# print(type("Number of letters in your name: "))


print("Number of letters in your name: " + str(length_of_user_name))
print(f"Number of letters in your name: {length_of_user_name}")