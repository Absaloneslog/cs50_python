
def main():
    user_greetting=input("Gretting: ").casefold().strip()
    user_greetting=is_there_hello(user_greetting)
    if user_greetting == 0:
        print(f"${user_greetting}")
    else:
        user_greetting = is_there_hey(user_greetting)
        print(f"${user_greetting}")

def is_there_hello(hello):
    position=hello.find("hello")
    if position == 0:
        return 0
    else:
        return hello

def is_there_hey(hey):
    position=hey.find("h")
    if position == 0:
        return 20
    else:
        return 100

main()
#submit50 cs50/problems/2022/python/bank