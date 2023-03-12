from .conversion_table import BIN_TO_HEX


class Binary():
    def __init__(self, binary_str: str) -> None:
        """Receives a string of 0's and 1's representing a binary number and converts it to
        decimal and hexadecimal values by calling the methods binary_to_decimal
        and binary_to_hex in the constructor_

        Args:
            binary_value (str): _A string of 0's and 1's representing a binary number_

        Attributes:
            binary_str (str): _A string of 0's and 1's representing a binary number_
            number_of_bits (int): _The number of bits of the binary number_
            decimal (str): _The decimal value of the binary number_
            hexadecimal (str): _The hexadecimal value of the binary number_
        """
        self.binary_str = binary_str
        self.number_of_bits = len(self.binary_str)
        self.validate_input(binary_str)
        self.preprocess()
        self.binary_to_decimal()
        self.binary_to_hex()

    def validate_input(self, binary_str: str) -> None:
        """_Method to check if the input string is a binary number_

        Args:
            binary_str (str): _A string of 0's and 1's representing a binary number_

        Raises:
            ValueError: _If the input string is not a binary number_
        """
        try:
            int(binary_str, 2)
        except ValueError:
            raise ValueError(f"{binary_str} is not a binary number")

        if self.binary_str.isspace() or self.binary_str == '':
            raise ValueError("Empty string or string with only spaces is not a binary number")

    def preprocess(self) -> None:
        """_Method to add zeros to the left of the binary number to make it divisible by 4_
        """
        quantity_of_zeros_to_fill = 4 - (self.number_of_bits % 4)
        self.binary_str = '0' * quantity_of_zeros_to_fill + self.binary_str

    def binary_to_decimal(self) -> None:
        """_Method to convert a binary number to a decimal number_
        """
        partial_decimal_value = 0
        power = 0
        bits = self.binary_str[::-1]

        for bit in bits:
            current_power_of_two = 2 ** power
            partial_decimal_value += int(bit) * current_power_of_two
            power += 1

        self.decimal = str(partial_decimal_value)

    def binary_to_hex(self) -> None:
        """_Method to convert a binary number to a hexadecimal number_
        """
        group_of_four_bits = [self.binary_str[i:i+4]
                              for i in range(0, self.number_of_bits, 4)]

        hex_list = [BIN_TO_HEX[group]
                    for group in group_of_four_bits]

        self.hexadecimal = ''.join(hex_list)

    def to_decimal(self) -> str:
        """_Method to return the decimal value of the binary number_

        Returns:
            int: _The decimal value of the binary number_
        """
        return self.decimal

    def to_hex(self) -> str:
        """_Method to return the hexadecimal value of the binary number_

        Returns:
            str: _The hexadecimal value of the binary number_
        """
        return self.hexadecimal
