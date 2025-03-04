#the main function
def main():
    m=" "
    m=variable(m)
    if m==0:
        print("You have closed the calculator. Matanee")
    else:
        E=einstein_calculator(m)
        print(f"{E}")
        main()

def variable(m):
    m=int(input("m(Kg): "))
    return m

def einstein_calculator(m):
    k_e= (3*10**8)**2
    E=k_e*m
    return E


def welcome():
    print("Welcome to the Einstein calculator.")
    print("Please insert the mass as a whole number.")
    print("You're going to receive the amount of energy in Jules.")
    print("IMPORTANT: If you want to close it enter 0")
welcome()
main()
