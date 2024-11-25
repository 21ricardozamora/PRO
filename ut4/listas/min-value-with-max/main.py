def run(values: list) -> int:
    max_value = max(values)
    min_value = values[0]
    for value in values[1:]:
        if value <= max_value and value <= min_value:
            min_value = value
    return min_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
