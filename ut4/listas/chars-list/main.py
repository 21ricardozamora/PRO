def run(texts: list) -> list:
    chars = []
    for text_index in texts:
        for char in text_index:
            if char in text_index:
                chars.append(char)
    return chars


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
