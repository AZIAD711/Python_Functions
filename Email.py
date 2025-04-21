from termcolor import colored
#FUNCTION TO GENERATE EMAIL
def GENERATE_EMAIL(NAME_CHECK,LETTER,NAME):
    NAME_CHECK={"A_NAME":"A","B_NAME":"B","C_NAME":"C","D_NAME":"D","E_NAME":"E","F_NAME":"F","G_NAME":"G","H_NAME":"H","I_NAME":"I","J_NAME":"J","K_NAME":"K","L_NAME":"L","M_NAME":"M","N_NAME":"N","O_NAME":"O","P_NAME":"P","Q_NAME":"Q","R_NAME":"R","S_NAME":"S","T_NAME":"T","U_NAME":"U","V_NAME":"V","W_NAME":"W","X_NAME":"X","Y_NAME":"Y","Z_NAME":"Z"}
    if (LETTER==NAME_CHECK["A_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}1111@gmail.com")
    elif (LETTER==NAME_CHECK["B_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}2121@gmail.com")
    elif (LETTER==NAME_CHECK["C_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}3232@gmail.com")
    elif (LETTER==NAME_CHECK["D_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}4343@gmail.com")
    elif (LETTER==NAME_CHECK["E_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}5454@gmail.com")
    elif (LETTER==NAME_CHECK["F_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}6565@gmail.com")
    elif (LETTER==NAME_CHECK["G_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}7676@gmail.com")
    elif (LETTER==NAME_CHECK["H_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}8787@gmail.com")
    elif (LETTER==NAME_CHECK["I_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}9898@gmail.com")
    elif (LETTER==NAME_CHECK["J_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}109109@gmail.com")
    elif (LETTER==NAME_CHECK["K_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}11101110@gmail.com")
    elif (LETTER==NAME_CHECK["L_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}121112@gmail.com")
    elif (LETTER==NAME_CHECK["M_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}13121312@gmail.com")
    elif (LETTER==NAME_CHECK["N_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}14131413@gmail.com")
    elif (LETTER==NAME_CHECK["O_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}15141514@gmail.com")
    elif (LETTER==NAME_CHECK["P_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}16151615@gmail.com")
    elif (LETTER==NAME_CHECK["Q_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}17161716@gmail.com")
    elif (LETTER==NAME_CHECK["R_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}18171817@gmail.com")
    elif (LETTER==NAME_CHECK["S_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}19181918@gmail.com")
    elif (LETTER==NAME_CHECK["T_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}20192019@gmail.com")
    elif (LETTER==NAME_CHECK["U_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}21202120@gmail.com")
    elif (LETTER==NAME_CHECK["V_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}22212221@gmail.com")
    elif (LETTER==NAME_CHECK["W_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}23222322@gmail.com")
    elif (LETTER==NAME_CHECK["X_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}24232423@gmail.com")
    elif (LETTER==NAME_CHECK["Y_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}25242524@gmail.com")
    elif (LETTER==NAME_CHECK["Z_NAME"]):
        return(f"EXPEXTED EMAIL IS : {NAME}26252625@gmail.com")
    else:
        print(colored("ERROR: YOU SHOULD ENTER LETTER : TRY AGAIN ! ",'white','on_red',attrs=['bold']))
#EXAMPLE IF YOU WISH TO TEST FUNCTION 
Name=input("PLEASE ENTER YOUR NAME : ").upper()
Letter=input("PLEASE ENTER WHICH LETTER YOU LIKE : ").upper()
if len(Letter)>1:
    while len(Letter)>1:
     print(colored("ERROR: MAXLENGTH OF LETTER IS 1 : TRY AGAIN ! ",'white','on_red',attrs=['bold']))
     Letter=input("PLEASE ENTER WHICH LETTER YOU LIKE : ").upper()
     if len(Letter)<=1:
        print(colored(f"{GENERATE_EMAIL(Name,Letter,Name)}",'white','on_green',attrs=['bold']))
else:
    print(colored(f"{GENERATE_EMAIL(Name,Letter,Name)}",'white','on_green',attrs=['bold']))

