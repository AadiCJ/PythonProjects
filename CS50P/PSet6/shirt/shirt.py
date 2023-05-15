import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext


def main():
    if isValid(sys.argv):
        imageProcess(sys.argv[1], sys.argv[2])


def isValid(args):
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    if len(args) > 3:
        sys.exit("Too many command-line arguments")

    file1, extension1 = splitext(args[1])
    file2, extension2 = splitext(args[2])

    if extension1 != extension2:
        sys.exit("Input and output have different extensions")

    if extension1 != ".png" and extension1 != ".jpg" and extension1 != ".jpeg":
        sys.exit("Invalid input")
    if extension2 != ".png" and extension2 != ".jpg" and extension2 != ".jpeg":
        sys.exit("Invalid input")

    return True


def imageProcess(inputPath, outputPath):
    shirt = Image.open("shirt.png")

    try:
        inputImg = Image.open(inputPath)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtSize = shirt.size

    imageFit = ImageOps.fit(inputImg, shirtSize)

    imageFit.paste(shirt, shirt)
    imageFit.save(outputPath)


if __name__ == "__main__":
    main()
