def run(words: list) -> str:
    valid_item = words[0]
    size_item = len(set(valid_item))
    dword = ''
    for item in words:
        if size_item < len(set(item)):
            valid_item = item
            size_item = len(set(valid_item))

    dword = valid_item

    return dword


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
