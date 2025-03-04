def main():
    user_file=input(f"File name: ").casefold().strip()
    user_file=cleaner(user_file)
    user_file=file_disc(user_file)
    print(f"{user_file}")

def cleaner(file):
    file=file.split(" ")
    file="".join(file)
    return file

#.gif.jpg.jpeg.png.pdf.txt.zip
def file_disc(file):
    if ".py" in file:
        return "program/python"
    elif ".gif" in file:
        return "image/gif"
    elif ".jpg" in file:
        return "image/jpeg"
    elif ".jpeg" in file:
        return "image/jpeg"
    elif ".png" in file:
        return "image/png"
    elif ".pdf" in file:
        return "application/pdf"
    elif ".txt" in file:
        return "text/plain"
    elif ".zip" in file:
        return "application/zip"
    else:
        return "application/octet-stream"
main()
#check50 cs50/problems/2022/python/extensions
