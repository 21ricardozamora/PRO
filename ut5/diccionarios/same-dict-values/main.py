def run(items: dict) -> bool:
    all_same = True
    for item in items:
        value_items = items.get(item)
        for _ in items.values():
            if value_items != _:
                all_same = False
            break
    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
