def run(values: list) -> int:
    min_value = min(values)
    max_value = values[0]
    for value in values:
        if value > min_value and value > max_value:
            max_value = value
    return max_value


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
