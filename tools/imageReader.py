from PIL import Image
from sys import argv
import io

def main():
    image = Image.open(argv[1])
    output = io.BytesIO()
    image.save(output, format="jpeg")
    image_as_string = output.getvalue()
    print(image_as_string.decode("utf-8"))
main()
