print("Please use whatever of the following formats  example:")
print("##:## HH:MM or ##:## a.m.")
def main():
    time(convert(get_hour()))

def get_hour():
    while True:
        hour=input("What time is it= ").strip()
        hour=hour.replace(" ", "")
        digit=hour.removesuffix("a.m.")
        digit=digit.removesuffix("p.m.")
        digit_hour=digit.replace(":", "")
        if "" == hour:
            break
        elif digit_hour.isnumeric()==True and ":" in hour:
            break
        else: 
            print("Is not the correct format")
            continue
    return hour

def convert(h):
    if "" == h:
        return h
    elif "a.m." in h:
        h=h.removesuffix("a.m.")
        x,y=h.split(":")
        x=int(x)
        y=int(y)/60
        if x == 12:
            x-=12
            return x+y
        else:
            return x+y
    elif "p.m." in h:
        h=h.removesuffix("p.m.")
        x,y=h.split(":")
        x=int(x)+12
        y=int(y)/60
        if x == 24:
            x-=12
            return x+y
        else:
            return x+y
    else:
        x,y=h.split(":")
        x=int(x)
        y=int(y)/60
        return x+y

def time(n):
    if n=="":
        print(f"")
    elif  7<=n<=8:
        print(f"breakfast time")
    elif 12<= n <=13:
        print(f"lunch time")
    elif 18<= n <=19:
        print(f"dinner time")
    else:
        print(f"")

if __name__ == "__main__":
    main()

