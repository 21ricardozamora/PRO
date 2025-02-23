def split_case(words: list[str]):
    upper_case = []
    lower_case = []
    for word in words:
        if word == word.upper() and word not in upper_case:
            upper_case.append(word)
        elif word == word.lower() and word not in lower_case:
            lower_case.append(word)
    return lower_case, upper_case


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
