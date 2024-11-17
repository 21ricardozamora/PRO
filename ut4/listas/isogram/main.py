def run(text: str) -> bool:
    isogram = True
    new_text = text.replace('-', '')
    unique_words = []
    while isogram:
        for char in new_text.lower():
            if char not in unique_words:
                unique_words.append(char)
            else:
                isogram = False
                break
        if len(new_text) == len(unique_words):
            isogram = True
            break
    return isogram


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
