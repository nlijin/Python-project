a = 0
b = 1
for i in range(20):
    if b<1:
        print("0")
    else:
        temp = a+b
        a=b
        b=temp
        print(temp)

