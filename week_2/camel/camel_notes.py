def main():
    camel_case=input(f"camelCase: ").strip()
    camel_case=camel_case.replace("", " ")
    camel_case=camel_case.split()
    print(f"{convert_snake_case(camel_case)}")

def convert_snake_case(letters):
    a=0
    while a<len(letters):
        if str(letters[a]).isupper():
            letters[a]="_"+str(letters[a]).lower()
        else:
            a+=1
    return "".join(letters)

main()