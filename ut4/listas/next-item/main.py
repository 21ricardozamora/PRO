def run(items: list, ref_item: object) -> object:
    if ref_item not in items:
        target_item = None
    else:
        index_item = items.index(ref_item)
    for item in items:
        if ref_item == items[-1]:
            target_item = None
            break
        else:
            if item == ref_item:
                target_item = items[index_item + 1]
                break
    return target_item


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
