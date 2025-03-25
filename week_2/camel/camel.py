#for c in s:
#    print(c, end="")
def main():
    camel_case=input(f"camelCase: ").strip()
    print(f"snake_case: {convert_snake_case(camel_case)}")

def convert_snake_case(letters):
    letters=letters.replace("", " ")
    letters=letters.split()
    a=0
    while a < len(letters):
        if str(letters[a]).isupper():
            letters[a]="_"+str(letters[a]).lower()
        else:
            a+=1
    return "".join(letters)

main()