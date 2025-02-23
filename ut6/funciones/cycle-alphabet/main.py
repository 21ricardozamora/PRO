def cycle_alphabet(num_chars: int) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    for char in range(num_chars):
        letter = char % len(ALPHABET)
        yield ALPHABET[letter]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(cycle_alphabet)
