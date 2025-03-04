print("The Deep Thought Program")
print("What is the Answer to the Great Question of Life,")
print("the Universe, and Everything?")
def main():
    user_answer=input("Enter your answer to the machine: ").lower()
    match user_answer:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")
main()