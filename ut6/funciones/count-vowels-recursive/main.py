def count_vowels(text: str) -> int:
    VOWELS = 'aeiouàèìòùáéíóú'
    num_vowels = 0
    if len(text) == 0:
        return 0
    num_vowels = 1 if text.lower()[0] in VOWELS else 0
    return num_vowels + count_vowels(text.lower()[1:])


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(count_vowels)
