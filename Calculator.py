def opr():
    "Operations"
    print("1. Addition","            2. Subtraction")
    print("3. Multiplication","      4. Division")
    return()
#------------------------
def add(a,b):
    "Performs Addition"
    x = a+b
    return(x)
#------------------------
def sub(a,b):
    "Performs Subtraction"
    x = a-b
    return(x)
#------------------------
def mult(a,b):
    "Performs Multiplication"
    x = a*b
    return(x)
#------------------------
def div(a,b):
    "Performs Division"
    x = a/b
    return(x)
#------------------------
print(opr())
q = str(input("Press Y Key To Continue or Press Q To Quit The Program"))

while(q=="y" or q=="Y"):
    t = str(input("Enter The Operation You Want To Perform :"))
    num1 = float(input("Enter First Number :"))
    num2 = float(input("Enter Second Number :"))
    if(t=="Addition" or t=="addition" or t=="add" or t=="Add" or t=="+" or t=="1"):
        print("Answer Is")
        print(add(num1,num2))
        q = str(input('Press Y Key For Using Calculator Again or Press "Q" To Quit The Program'))
    
    if(t=="Subtraction" or t=="subtraction" or t=="sub" or t=="Sub" or t=="-" or t=="2"):
        print("Answer Is")
        print(sub(num1,num2))
        q = str(input('Press Y Key For Using Calculator Again or Press "Q" To Quit The Program'))

    if(t=="Multiplication" or t=="multiplication" or t=="mul" or t=="Mul" or t=="*" or t=="3"):
        print("Answer Is")
        print(mult(num1,num2))
        q = str(input('Press Y Key For Using Calculator Again or Press "Q" To Quit The Program'))
    
    if(t=="Division" or t=="division" or t=="div" or t=="Div" or t=="/" or t=="4"):
        print("Answer Is")
        print(div(num1,num2))
        q = str(input('Press Y Key For Using Calculator Again or Press "Q" To Quit The Program'))
    
print("\nThanks For Using The Calculator.","\n\nGOOD BYE! HAVE A NICE DAY")
