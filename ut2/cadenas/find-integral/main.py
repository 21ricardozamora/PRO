def run(symbol: str) -> str:
    symbol_separator = symbol.find(',')
    coefficent = int(symbol[:symbol_separator])
    exponent = int(symbol[symbol_separator + 1 :])
    exponent = exponent + 1
    new_coefficent = coefficent // exponent
    integral = f'{new_coefficent}x^{exponent}'
    return integral


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
