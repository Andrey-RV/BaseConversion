from base_conversion import binary
from base_conversion import hexadecimal


def main():
    binary_number = binary.Binary('1010101')
    print(binary_number.to_decimal())
    print(binary_number.to_hex())

    hex_number = hexadecimal.Hexadecimal('A2C')
    print(hex_number.to_decimal())
    print(hex_number.to_binary())

if __name__ == '__main__':
    main()
