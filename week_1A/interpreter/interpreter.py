def main():
    print("x operator z")
    x,y,z =input().split(" ")
    approval_value=check_in(x,y,z)
    match approval_value:
        case "No 1": 
            print("x has to be an integer")
        case "No 2":
            print("z has to be an integer")
        case "No 3":
            print("You can't get divided by 0")
        case "Yes":
            value=calculator(x,y,z)
            print(f"{value:.1f}")

def check_in(x,y,z):
    x=x.strip("-")
    z=z.strip("-")
    if x.isalpha():
        return "No 1"
    elif z.isalpha():
        return "No 2"
    elif z=="0" and y=="/":
        return "No 3"
    else:
        return "Yes"
        

def calculator(x,y,z):
    x=float(x)
    z=float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*" :
        return x * z
    elif y == "/":
        return x / z
    else:
        return "Try again in this format x + z"
main()

