def bsort(values: list[int]) -> list:
    copy_values = []
    for item in values:
        first_item = values[0]
        if item < first_item:
            first_item = item
            copy_values.append(first_item)
    return copy_values


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(bsort)
