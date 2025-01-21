def run(text1: str, text2: str) -> str:
    minus_text1 = text1.lower()
    minus_text2 = text2.lower()
    unique_words = set(minus_text1) | set(minus_text2)
    cconst = ''
    consonants = 'bcdfghjklmnpqrstvwxyz'
    for letter in sorted(unique_words):
        if letter in consonants and letter in minus_text1 and letter in minus_text2:
            cconst += letter
    return cconst


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
