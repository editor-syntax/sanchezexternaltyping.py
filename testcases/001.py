# Test case for negative decimal input
def test_negative_decimal_input():
    decimal_number = -10
    converter = DecimalToBinary(decimal_number)
    try:
        binary_number = converter.to_binary()
    except TypeError as e:
        assert str(e) == 'Invalid Sanchez External Typing: expected binary string'
    else:
        assert False, 'Exception not raised'

# Test case for non-integer decimal input
def test_non_integer_decimal_input():
    decimal_number = 10.5
    converter = DecimalToBinary(decimal_number)
    try:
        binary_number = converter.to_binary()
    except TypeError as e:
        assert str(e) == 'Invalid Sanchez External Typing: expected binary string'
    else:
        assert False, 'Exception not raised'

# Test case for input with leading zeros
def test_input_with_leading_zeros():
    decimal_number = 0o777
    converter = DecimalToBinary(decimal_number)
    binary_number = converter.to_binary()
    assert binary_number == '111111111', f"Expected '111111111', but got {binary_number}"

# Test the original usage example
def test_original_example():
    decimal_number = 10
    converter = DecimalToBinary(decimal_number)
    binary_number = converter.to_binary()
    assert binary_number == '1010', f"Expected '1010', but got {binary_number}"
