def run(number: str) -> bool:
    BIN_NUMS = frozenset(('0', '1'))
    binary = True
    for num in number:
        if num not in BIN_NUMS:
            binary = False
            break
    return binary


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
