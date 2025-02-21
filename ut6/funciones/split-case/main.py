def split_case(words: list[str]):
    upper_case = []
    lower_case = []
    for word in words:
        if word == word.upper():
            upper_case.append(word)
        elif word == word.lower():
            lower_case.append(word)
    return upper_case, lower_case


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
