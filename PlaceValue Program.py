def placevalue(x):
    y = len(str(abs(x)))
    if(y==1):
        print("Unit")
    if(y==2):
        print("Ten")
    if(y==3):
        print("Hundred")
    if(y==4):
        print("Thousand")
    if(y==5):
        print("Ten Thousand")
    if(y==6):
        print("Hundred Thousand")
    return(y)

num = int(input("Enter number :"))
print(placevalue(num))
