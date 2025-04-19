def ADD(NUMBER):
    SUM=0
    for COUNT in range(1,NUMBER+1):
        SUM+=float(input(f"ENTER NUMBER ({COUNT}) : "))
    return SUM