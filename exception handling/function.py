# def multi_table(n):
#     for i in range(1,11):
#         if i<10:
#             # print("",i,"*",n,"=",i*n)
#             print(f"{i} * {n} = {i*n}")
#         else:
#             print(i,"*",n,"=",i*n)
# num=int(input("Enter number for table : "))
# multi_table(num)


def fibb(n,a,b): 
    c=0 
    while b<=n:
        c=a+b
        print(b,end=" ")
        a=b
        b=c


a=0
b=1
print(a,end=" ") 
fibb(10,a,b)
print("\n")
def swap(a,b):
    a,a=a,b
    print(a,b)

swap(4,6)