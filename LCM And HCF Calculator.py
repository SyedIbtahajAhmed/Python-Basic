#========================
#========================
def gcd(a,b):
    "Calculates GCD Of Two Numbers"
    if(b==0):
        return a
    return gcd(b, a%b)
#========================
#========================
def lcm(a,b):
    "Calculates LCM Of Two Numbers"
    y = (a*b)/gcd(a,b)
    return(y)
#========================
#========================
def hcf(a,b):
    "Calculates HCF Of Two Numbers"
    y = a*b/lcm(a,b)
    return(y)
#========================
#========================
def opr():
    "Operations"
    print("1. H.C.F(Highest Common Factor)")
    print("2. L.C.M(Least Common Multiple)")
    print("3. G.C.D(Greatest Common Divisor)")
#========================
#========================
print(opr())
p = str(input("Press Y To Enter Values Of Two Numbers Or Press Q To Quit The Program"))

while(p=="y" or p=="Y"):
    x = float(input("Enter First Number :"))
    y = float(input("Enter Second Number :"))
    print("\n* Highest Common Factor (H.C.F) is      ",hcf(x,y))
    print("\n* Least Common Multiple (L.C.M) is      ",lcm(x,y))
    print("\n* Greatest Common Divisor (G.C.D) is    ",gcd(x,y))
    p = str(input("Press Y To Enter Values Of Two Numbers Or Press Q To Quit The Program"))
print("THANKS FOR USING!","\nGOOD BYE")
