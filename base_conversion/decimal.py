from .conversion_table import DEC_TO_HEX


class Decimal():
    def __init__(self, decimal_input: str | int) -> None:
        """_Receives an int or a string representing a decimal number and converts it to binary and hexadecimal
        values by calling the methods decimal_to_binary and decimal_to_hex in the constructor_

        Args:
            decimal_input (str | int): _An int or a string representing a decimal number_

        Attributes:
            decimal_str (str): _A string representing a decimal number_
            binary_str (str): _A string representing a binary number_
            hex_str (str): _A string representing a hexadecimal number_
        """
        self.decimal_str = str(decimal_input)
        self.validate_input(self.decimal_str)
        self.decimal_to_binary()
        self.decimal_to_hex()

    def validate_input(self, decimal_str: str) -> None:
        """_Method to check if the input string is a decimal number_

        Args:
            decimal_str (str): _A string representing a decimal number_

        Raises:
            ValueError: _If the input string is not a decimal number_
        """
        try:
            int(decimal_str)
        except ValueError:
            raise ValueError(f"{decimal_str} is not a decimal number")

        if not self.decimal_str.isdigit():
            raise ValueError(f"{decimal_str} is not a decimal number")

    def decimal_to_binary(self) -> None:
        """_Method to convert a decimal number to a binary number by successively dividing the number by 2_"""
        decimal_value = int(self.decimal_str)
        binary_value = ''

        while decimal_value > 0:
            binary_value += str(decimal_value % 2)
            decimal_value //= 2

        self.binary_str = binary_value[::-1]

    def decimal_to_hex(self) -> None:
        """_Method to convert a decimal number to a hexadecimal number by successively dividing the number by 16_"""
        decimal_value = int(self.decimal_str)
        hex_value = ''

        while decimal_value > 0:
            hex_value += DEC_TO_HEX[str(decimal_value % 16)]
            decimal_value //= 16

        self.hex_str = hex_value[::-1]

    def to_binary(self) -> str:
        """_Method to return the binary value of the decimal number_

        Returns:
            str: _A string representing a binary number_
        """
        return self.binary_str

    def to_hex(self) -> str:
        """_Method to return the hexadecimal value of the decimal number_

        Returns:
            str: _A string representing a hexadecimal number_
        """
        return self.hex_str
