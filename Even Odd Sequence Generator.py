#================================
#================================
def even(start,stop):
    "Generates Even Sequence"
    while(start<=stop):
        if(start%2==0):
            print(start)
            start+=2
        else:
            start+=1
            print(start)
            start+=2
            
    while(stop<=start):
        if(start%2==0):
            print(start)
            start = start-2
        else:
            start = start-1
            print(start)
            start = start-2
    return
#=================================
#=================================
def odd(start,stop):
    "Generates Odd Sequence"
    while(start<=stop):
        if(start%2!=0):
            print(start)
            start+=2
        else:
            start+=1
            print(start)
            start+=2
    while(stop<=start):
        if(start%2!=0):
            print(start)
            start = start-2
        else:
            start = start-1
            print(start)
            start = start-2
    return
#================================
#================================
i = str(input("Press Y Key To Continue or Press Q to Quit The Program :"))
while(i=="y" or i=="Y"):
    op = str(input("What Do You Want To Generate Even Sequence Or Odd Sequence :"))
    x = int(input("Input The Starting Value :"))
    y = int(input("Input The Ending Value :"))
    if(op=="even" or op=="Even"):
        print(even(x,y))
        print("THANKS FOR USING!")
        i = str(input("Press Y Key To Again Enter Values or Press Q to Quit The Program :"))
    if(op=="odd" or op=="Odd"):
        print(odd(x,y))
        print("THANKS FOR USING!")
        i = str(input("Press Y Key To Again Enter Values or Press Q to Quit The Program :"))
print("THANKS FOR USING!","\nHAVE A NICE DAY","\nGOOD BYE!")
