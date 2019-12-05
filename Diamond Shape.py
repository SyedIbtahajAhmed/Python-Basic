z = str(input('Press "Y" To Make The Diamond Shape and "Q" to Quit The Program.'))
while(z=="Y" or z=="y"):
    char = str(input("\nEnter any Character you want to make the diamond shape with :"))
    leng = int(input("\nEnter Size Of Shape In Lines :"))
    spac = " "
    b = 0
    char1 = char
    leng1 = leng
    a = 1
    char2 = char
    leng2 = leng
    char3 = char
    leng3 = leng
    c = 1
    d = leng*2-2
    for x in range(0,leng):
        print(char*leng,spac*b,char2*leng2)
        leng = leng-1
        leng2 = leng2-1
        b = b+2
    for y in range(0,leng1):
        print(char1*a,spac*d,char3*c)
        a+=1
        c = c+1
        d = d-2
    z = input('\nPress "Y" To Make The Diamond Shape and "Q" to Quit The Program.')
print("Thanks For Using!")
