def is_pangram(text: str) -> bool:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    clean_text = text.replace(' ', '').lower()
    chars = []
    pangram = True
    for char in clean_text:
        if char not in chars and char.isalpha():
            chars.append(char)
    if len(ALPHABET) != len(chars):
        pangram = False
    return pangram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_pangram)
