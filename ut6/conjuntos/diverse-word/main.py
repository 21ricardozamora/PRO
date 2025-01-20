def run(words: list) -> str:
    dword = ''
    for item in words:
        valid_item = item
        len_item = len(set(valid_item))
        if len_item < len(set(item)):
            valid_item = item
        dword = valid_item

    return dword


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
