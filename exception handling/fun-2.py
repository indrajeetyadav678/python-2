

def pellin(n):
    temp=n
    cp=0
    while temp>0:
        last=temp%10
        cp=(cp*10)+last
        temp=temp//10
    if cp == n:
        return "yes" 
    else:
        return "No"

pellin(560)


def arm(n1):
    temp=n1
    sum=0
    digit=n1
    l=len(str(digit))
    while temp>0:
        last=temp%10
        sum=sum+(last**l)
        # print("sum =",sum)
        temp=temp//10
        # print("temp =", temp)

    if sum==n1:
        return "yes"
    else:
        return "No"
    
# print(arm(151))

for i in range(11,1000,1):
    ans=arm(i)
    ans2=pellin(i)
    # print(ans)
    if ans=="yes":
        print("armstrong =",i)
    if ans2=="yes":
        print("pallindrome number =",i)


