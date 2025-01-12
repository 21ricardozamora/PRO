def run(items: list) -> dict:
    unpack_items = {}
    keys_item = ''
    values_item = []
    for item in items:
        if item[0] not in keys_item:
            keys_item = item[0]
            values_item = item[1:]
            unpack_items[keys_item] = values_item
    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
