def run(words: list) -> str:
    reference_word = words[0]
    size_reference_word = len(set(reference_word))
    dword = ''
    for word in words:
        size_word = len(set(word))
        if size_reference_word < size_word:
            reference_word = word
            size_reference_word = size_word
    dword = reference_word

    return dword


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
