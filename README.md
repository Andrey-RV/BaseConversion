# Base Converstion
This is a package made as a learning project containing classes and methods to convert a value between binary, decimal and hexadecimal without using the standart conversion using the int() class.

## Requirements
To run the program, you'll need Python 3.9 or above to avoid any errors related to Type Hints from PEP 585. To start, download or clone the repository, and navigate to the project directory

```
cd BaseConversion
```

## How to use
In a new empty .py file, import the binary, decimal and hexadecimal modules

```
from base_conversion import binary, decimal, hexadecimal
```

### Converting from binary
Instatiate a Binary object passing either a str or an int representation of a binary number
```
binary_number = binary.Binary(101101)
```

The decimal and hexadecimal values are returned from the methods to_decimal() and to_hexadecimal()
```
decimal_value = binary_number.to_decimal()
#45

hex_value = binary_number.to_hexadecimal()
#2D
```

### Converting from decimal
Instatiate a Decimal object passing either a str or an int representation of a decimal number
```
decimal_number = binary.Decimal('45')
```

The binary and hexadecimal values are returned from the methods to_binary() and to_hexadecimal()
```
decimal_value = decimal_number.to_binary()
#101101

hex_value = decimal_number.to_hexadecimal()
#2D
```

### Converting from hexadecimal
Instatiate a Hexadecimal object passing a str representation of a hexadecimal number
```
hex_number = binary.Binary('2D')
```

The binary and decimal values are returned from the methods to_binary() and to_decimal()
```
binary_value = hex_number.to_binary()
#00101101

decimal_value = hex_number.to_decimal()
#45
```

## Documentation
The documentation about the implementation can be found [here](https://andrey-rv.github.io/BaseConversion/)
