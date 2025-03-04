#promt numbers for x and y
#x = input("What is x?  ")
#y = input("What is y?  ")
#convert str to integer


#Add numbers
#z= int(x) + int(y)
#output
#print(z)

#----------------------------------------------------------------
#promt numbers for x and y then convert to int
#x=int(input("What is x? "))
#y=int(input("What is y? "))

#Add numbers
#z= x+y

#output
#print(z)
#-------------------------------------------------------------
#def calculator_dive():
#    x = input("What is x?  ")
#    if type(float(x)) == float:
#        y = input("What is y?  ")
#            if type(float(y)) == float:
#                print(float(x)/float(y))
#            else:
#                print("y has to be a number")
#                calculator_dive()
#    else:
#        print("X has to be a number")
#        calculator_dive() 
def calculator(x,y):
    z = x / y
    print(f"{z:2f}")


x = float(input("What is x? "))
y = float(input("What is y? "))

calculator(x,y)