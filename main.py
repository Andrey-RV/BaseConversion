from .base_conversion import binary


def main():
    binary_number = binary.Binary('1010101')
    print(binary_number.to_decimal())
    print(binary_number.to_hex())


if __name__ == '__main__':
    main()
