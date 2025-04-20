#FUNCTION TO MINUS NUMBERS 
def min(NUMBER):
    M=float(input("ENTER NUMBER (1) : "))
    for COUNT in range(2,NUMBER+1):
        M-=float(input(f"ENTER NUMBER ({COUNT}) : "))
    return M
#EXAMPLE IF YOU WISH TO TEST FUNCTION 
N=int(input("ENTER NUMBER TO MINUS : "))
print(f"TOTAL = {min(N)}")