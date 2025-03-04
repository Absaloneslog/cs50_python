name=input()
match name:
    case "Harry" | "Hermione"|"Ron":
        print("Griffyndor")
    case _:
        print("Who?")
print(name.append("Hermione"))