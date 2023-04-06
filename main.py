from functools import wraps

def sanchez_external_typing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str) or not all(c in '01' for c in result):
            raise TypeError('Invalid Sanchez External Typing: expected binary string')
        return result
    return wrapper

class DecimalToBinary:
    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    @sanchez_external_typing
    def to_binary(self):
        return bin(self.decimal_number)[2:]

# Usage
decimal_number = 10
converter = DecimalToBinary(decimal_number)
binary_number = converter.to_binary()
print(f"The binary representation of {decimal_number} is {binary_number}")
