import os

# f= open("./practice-2/file_handling/ftext.txt","w")
# f.write("this file handing method")
# f.close()

# f=open("./practice-2/file_handling/ftext.txt","a")
# f.write("\n yor are doing file hendling work")
# f.close

# f= open("ftext.txt","r")
# print(f.read())

# os.remove("./practice-2/file_handling/ftext.txt")

import os

if os.path.exists("ftext.txt"):
    os.remove("ftext.txt")
else:
    print("File does not exist")
