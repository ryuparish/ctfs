import base64
from sys import argv

def main():
    # argv[0] is the filename argv[1] is the argument
    base64_message = argv[1]
    print("Here is the input: ", base64_message)
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)
main()
