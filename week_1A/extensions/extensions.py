def main():
    user_file=input(f"File name: ").casefold().strip()
    user_file=cleaner(user_file)
    user_file=file_disc(user_file)
    print(f"{user_file}")

def cleaner(file):
    file=file.split(" ")
    file="".join(file)
    return file

def file_disc(file):
    if ".py" in file:
        return "program/python"
    elif".jpg" in file:
        return "image/jpg"

main()