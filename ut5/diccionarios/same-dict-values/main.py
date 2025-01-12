def run(items: dict) -> bool:
    all_same = True
    for item in items:
        value_item = items.get(item)
        for item in items.values():
            if item != value_item:
                all_same = False
                break
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
