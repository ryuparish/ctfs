import binascii
from sys import argv

def main():
    binary_int = int(argv[1], 2)
    byte_number = binary_int.bit_length() + 7 // 8
    
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    
    print(ascii_text)
main()
