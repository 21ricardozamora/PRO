def run(values: list, ref_value: int) -> list:
    values_bigger_than_ref_value = []
    values_lower_than_ref_value = []
    for value in values:
        if value >= ref_value:
            values_bigger_than_ref_value.append(value)
        else:
            values_lower_than_ref_value.append(value)
    vpartition = [values_lower_than_ref_value, values_bigger_than_ref_value]
    return vpartition


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
