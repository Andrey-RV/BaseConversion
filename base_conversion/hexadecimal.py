from .conversion_table import HEX_TO_BIN


class Hexadecimal():
    def __init__(self, hex_str: str) -> None:
        """Receives a string representing a hexadecimal number and converts it to
        decimal and binary values by calling the methods hex_to_decimal
        and hex_to_binary in the constructor_

        Args:
            hex_str (str): _A string representing a hexadecimal number_

        Attributes:
            hex_str (str): _A string representing a hexadecimal number_
            decimal (str): _The decimal value of the hexadecimal number_
            binary (str): _The binary value of the hexadecimal number_
        """
        self.hex_str = hex_str
        self.validate_input(hex_str)
        self.hex_to_decimal()
        self.hex_to_binary()

    def validate_input(self, hex_str: str) -> None:
        """_Method to check if the input string is a hexadecimal number_

        Args:
            hex_str (str): _A string of hexadecimal digits_

        Raises:
            ValueError: _If the input string is not a hexadecimal number_
        """
        try:
            int(hex_str, 16)
        except ValueError:
            raise ValueError(f"{hex_str} is not a hexadecimal number")

        if self.hex_str.isspace() or self.hex_str == '':
            raise ValueError("Empty string or string with only spaces is not a hexadecimal number")

    def hex_to_binary(self) -> None:
        """_Method to convert a hexadecimal number to a binary number_
        """
        binary_str = [HEX_TO_BIN[digit] for digit in self.hex_str]
        self.binary = ''.join(binary_str)

    def hex_to_decimal(self) -> None:
        """_Method to convert a hexadecimal number to a decimal number_
        """
        hex_no_letters_reversed = self.preprocess()
        partial_decimal_value = 0
        power = 0

        for digit in hex_no_letters_reversed:
            partial_decimal_value += digit * 16 ** power
            power += 1
    
        self.decimal = str(partial_decimal_value)

    def preprocess(self) -> list[int]:
        """_Method to convert the hexadecimal digits to integers_

        Returns:
            list[int]: _A list of integers representing the hexadecimal digits. The letters A-F are converted to 10-15_
        """
        hex_list = [int(digit
                        .replace('A', '10')
                        .replace('B', '11')
                        .replace('C', '12')
                        .replace('D', '13')
                        .replace('E', '14')
                        .replace('F', '15')
                        )for digit in self.hex_str]

        hex_list.reverse()
        return hex_list
    
    def to_decimal(self) -> str:
        """_Method to return the decimal value of the hexadecimal number_

        Returns:
            str: _The decimal value of the hexadecimal number_
        """
        return self.decimal
    
    def to_binary(self) -> str:
        """_Method to return the binary value of the hexadecimal number_

        Returns:
            str: _The binary value of the hexadecimal number_
        """
        return self.binary
