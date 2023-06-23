# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# name = input("What is your name?\n")
with open("/Users/rajaa/Desktop/my_file.txt", mode="w") as file:
    file.write("My name is Muhammad Anwar Subhani.")

with open("../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
