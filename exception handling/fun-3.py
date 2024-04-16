

# c=230
# d=230

# if c==230:
#     print("first if state")
# elif d==230:
#     print("second if state")

# if '3' in str(c):
#     print(f"{3} is exist in {c}")
# else:
#     print(f"{3} is not exist in {c}")

# def findname(name):
#     global phonebook
#     if name in phonebook:
#         print(name)
#         del phonebook[name]
#         print("Phone number deleted for", name)
#     else:
#         print("Name not found in phonebook")

# def findname(name):
#     global phonebook
#     for i in list(phonebook):
#         print(i)
#         if i == name:
#             print(name)
#             del phonebook[name]
#             print("Phone number deleted for", name)
#         else:
#             print("Name not found in phonebook")

# # Example phonebook dictionary
phonebook = {"ajay": 9898989898, "aman": 8787878787, "raj": 9090909090}



print(phonebook)
# findname("aman")
# print("Updated phonebook:", phonebook)

for i in list(phonebook):
    print(i)
    if i=="aman":
        del phonebook[i]
print(phonebook)
print(type(phonebook))