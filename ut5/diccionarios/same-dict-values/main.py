def run(items: dict) -> bool:
    items_values = list(items.values())
    all_same = True
    for item in items_values:
        value = items_values[0]
        if value != item:
            all_same = False
            break
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
