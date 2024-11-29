def run(number: int) -> list:
    rev_digits = []
    for char in str(number):
        char = int(char)
        rev_digits.append(char)
    rev_digits = rev_digits[::-1]
    return rev_digits


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
