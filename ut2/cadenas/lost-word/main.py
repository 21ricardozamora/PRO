def run(text: str, target_word: str, replace_word: str) -> str:
    word_seeked = text.find(target_word)
    initial_text = text[:word_seeked]
    final_text = text[word_seeked + len(target_word) :]
    mtext = initial_text + replace_word + final_text
    return mtext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
