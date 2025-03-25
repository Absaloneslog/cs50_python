def main():
    names=["Mario", "Luigi", "Yoshi", "Toad"]
    for name in names:
        print(f"{write_letter(name, "Peach Princess")}")

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear, {receiver}
    
    You are cordially invited to a ball
    at Peach's Castle this evening, 
    7:00 PM.
    
    sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
main()