#1 Loops are a way to do something over and over again.
#2 Begin by typing code cat.py
#print("meow")
#print("meow")
#print("meow")
#A loop will repeat a block of code over and over again.

#i=3
#while i!=0:
#    print("meow")
#    i=i-1


#i=0
#while i<3:
#    print("meow")
#    i+=1


# a for loop itereates from a list of items like:
#for i in [0,1,2]:
#     print("for loop")

#for i in range(3):
#    print("range loop")

#print("without loop\n"*3, end="")

#while True:
#    n=int(input("What's n= "))
#    if n<0:
#        continue
#    else:
#        break

#while True:
#    num=input("What's n= ")
#   num_natural=num.strip("-")
#    value_n=num_natural.isdigit()
#    if value_n==True:
#        n=int(num)
#        print(f"{n}")
#        break
#    else:
#        continue

#def main():
#    bark(get_number())

#def get_number():
#    while True:
#        n=input("How many barks= ")
#        natural_n=n.strip("-")
#        n_is_digit=natural_n.isdecimal()
#        if n_is_digit==True:
#            break
#    while True:
#        num=int(n)
#        if num>0:
#            return num

#def bark(n):
#    for _ in range(n):
#        print("bark!")

#main()

#Dictionaries
#heroes={
#    "Invencible": "Mark",
#    "Spider-man": "Peter",
#    "Dupli-kate": "kate",
#    "4-arms": "Ben",
#    "Omni-man":"Nolan",
#    "kid Omni-man": "Oliver"
#}
#for i in heroes:
#    print(i)
def main():
    words={
    "pair":4, "chair":5, "hair":4, "graphic":7
    }
    print(f"Welcome to spelling bee")
    print(f"your letters are [ a, c, h , g, i, r, p ]")
    print("if you want to surrender write the word 'DRAW' ")
    game_loop(words)
    words.update({"pair":4, "chair":5, "hair":4, "graphic":7})
    for word in words.keys():
        print(f"{word} was worth {words[word]} points")

def game_loop(words):
    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess=input(f"What is your word?: ")
        if guess=="DRAW":
            words.clear()
            print(f"Game over")
        elif guess=="graphic":
            words.clear()
            print(f"You've won")
        elif guess in words.keys():
            points=words.pop(guess)
            print(f"Good job, you scored {points} points ")
        else:
            print(f"This is not the word")

main()

