def run(value1: int | float, value2: int | float, value3: int | float) -> int | float:
    if value1 < value2 and value3:
        min_value = value1
    if value2 < value3 and value1:
        min_value = value2
    if value3 < value2 and value1:
        min_value = value3
    if value1 == value2 and value3:
        min_value = value2
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
