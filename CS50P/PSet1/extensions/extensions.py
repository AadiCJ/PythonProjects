def main():
    str = input("Input your file name: ")  # str hold input
    str = (
        str.strip().lower()
    )  # get rid of trailing spaces and ensure case insensitivity
    if str.endswith(".gif"):
        print("image/gif")
    elif str.endswith(".jpeg") or str.endswith(".jpg"):
        print("image/jpeg")
    elif str.endswith(".png"):
        print("image/png")
    elif str.endswith(".pdf"):
        print("application/pdf")
    elif str.endswith(".txt"):
        print("text/plain")
    elif str.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
"""
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
"""
