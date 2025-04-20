#FUNCTION TO DIVIDE NUMBERS 
def DIVIDE(NUMBER):
    D=float(input("ENTER NUMBER (1) : "))
    for COUNT in range(2,NUMBER+1):
        D/=float(input(f"ENTER NUMBER ({COUNT}) : "))
    return D
#EXAMPLE IF YOU WISH TO TEST FUNCTION 
N=int(input("ENTER NUMBER TO DIVIDE : "))
print(f"TOTAL OF DIVIDE = {DIVIDE(N)}")