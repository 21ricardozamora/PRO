def run(text: str) -> int:
    num_words = len(text.split())
    # otra forma de hacerlo más entendible:
    # new_text = text.split()
    # num_words = len(new_text)
    return num_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
