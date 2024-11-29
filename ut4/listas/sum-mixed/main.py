def run(items: list) -> int:
    item = []
    for char in items:
        if isinstance(char, str):
            char = int(char)
        item.append(char)
    sum_items = sum(item)
    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
