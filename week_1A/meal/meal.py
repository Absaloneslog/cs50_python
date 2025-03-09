title="Meal timer"
print("Please use whatever of the following formats  example:")
print("##:## HH:MM or ##:## a.m.")
def main():
    # Ask for input.
    time=input(" What time is it? ").strip()
    time=time.replace(" ","")
    if time=="":
        print("")
    elif not ":" in time:
        print("Please use the format of the previous examples")
    else:
    #Checking the format
        approval=check_in(time)
        match approval:
            case "number_error":
                print("Please only use numbers")
            case "format_error":
                print("Please use the format of the previous examples")
            case "Yes":
                hour=convert(time)
                #print(f"{hour}")
                machine_answer=match_machine(hour)
                print(f"{machine_answer}")

def check_in(time):
    if "a.m." in time:
        time=time.strip("a.m.")
        x,y=time.split(":")
        if not (x.isdigit() and y.isdigit()):
            return "number_error"
        else:
            return "Yes"
    elif "p.m." in time:
        time=time.strip("p.m.")
        x,y=time.split(":")
        if not (x.isdigit() and y.isdigit()):
            return "number_error"
        else:
            return "Yes"
    else:
        x,y=time.split(":")
        if not (x.isdigit() and y.isdigit()):
            return "format_error"
        else:
            return "Yes"

def convert(time):
    if "a.m." in time:
        time_am=time.strip("a.m.")
        x,y=time_am.split(":")
        x=float(x)
        y=float(y)/60
        if x==12:
                x=x-12
                z=x+y
                return z
        else:
            z=x+y
            return z
    elif "p.m." in time:
        time_pm=time.strip("p.m.")
        x,y=time_pm.split(":")
        x=float(x)+12
        y=float(y)/60
        if x==24:
                x=float(x)-12
                z=x+y
                return z
        else:
            z=x+y
        return z
    else:
        x,y=time.split(":")
        x=float(x)
        y=float(y)/60
        z=x+y
        return z
#> y <
def match_machine(h):
    if  7<=h<=8:
        return "breakfast time"
    elif 12<=h<=13:
        return "lunch time"
    elif 18<=h<=19:
        return "dinner time"
    else:
        return ""

if __name__ == "__main__":
    main()



