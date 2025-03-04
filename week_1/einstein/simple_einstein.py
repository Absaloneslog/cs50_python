print("Welcome to Einstein calculator!")
print("Please enter the mass as a whole number.")
#DEF the main function E=mc^2
def einstein_calculator():
    m= input("m(kg): ")
    if m== 0:
        print("You have closed the calculator. Matanee")
    elif m.isdigit() == False:
        print("Please enter an Integer number")
        einstein_calculator()
    else:
        m= int(m)
        k_e= (3*10**8)**2
        E=m*k_e
        print(f"{E}")
einstein_calculator()
#check50 cs50/problems/2022/python/einstein

