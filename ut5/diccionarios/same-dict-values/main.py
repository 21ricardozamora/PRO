def run(items: dict) -> bool:
    values = []
    all_same = True
    for item in items.keys():
        value_item = items.get(item)
        if value_item not in values:
            values.append(value_item)
        if  != value_item:
            all_same = False
            break
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
