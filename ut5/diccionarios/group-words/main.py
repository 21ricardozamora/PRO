def run(words: list) -> dict:
    group_words = {}
    values = ''
    for item in words:
        key_group_words = item[0][0]
        if item != values:
            values = item

            group_words[key_group_words] = values
    return group_words


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
