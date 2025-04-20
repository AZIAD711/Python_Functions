#FUNCTION TO CALCULTOR NUMBERS 
def CAL(NUMBER,SIGN):
    SUM=0
    PRODUCT=1
    if SIGN == '+':
        for SUM_COUNT in range(1,NUMBER+1):
            SUM +=float(input(f"ENTER NUMBER ({SUM_COUNT}) : "))
        return SUM
    elif SIGN == '-':
        for COUNT in range(2,NUMBER+1):
            MINUS=float(input("ENTER NUMBER (1) : "))
            MINUS -=float(input(f"ENTER NUMBER ({COUNT}) : "))
        return MINUS
    elif SIGN == '*':
        for COUNT in range(1,NUMBER+1):
            PRODUCT *=float(input(f"ENTER NUMBER ({COUNT}) : "))
        return PRODUCT
    elif SIGN == '/':
        DIVIDE=float(input("ENTER NUMBER (1) : "))
        for COUNT in range(2,NUMBER+1):
            DIVIDE /=float(input(f"ENTER NUMBER ({COUNT}) : "))
        return DIVIDE
    elif SIGN == '**':
        N=int(input("ENTER NUMBER OF BASE : "))
        P=int(input("ENTER NUMBER OF POWER : "))
        POWER=pow(N,P)
        return POWER
#EXAMPLE IF YOU WISH TO TEST FUNCTION 
Number=int(input("ENTER NUMBER TO DIVIDE : "))
Sign=input("ENTER SIGN (+,-,*,/,**) : ")
print(f"TOTAL = {CAL(Number,Sign)}")