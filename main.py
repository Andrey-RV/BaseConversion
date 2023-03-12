from base_conversion import binary
from base_conversion import hexadecimal
from base_conversion import decimal


def main():
    binary_number = binary.Binary(1)
    print(binary_number.to_decimal())
    print(binary_number.to_hex())

    hex_number = hexadecimal.Hexadecimal('1')
    print(hex_number.to_decimal())
    print(hex_number.to_binary())

    decimal_number = decimal.Decimal(1)
    print(decimal_number.to_binary())
    print(decimal_number.to_hex())


if __name__ == '__main__':
    main()
