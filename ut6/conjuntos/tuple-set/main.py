def run(input: tuple) -> tuple[set, set]:
    value1 = set()
    value2 = set()
    for item1, item2 in input:
        value1.add(item1)
        value2.add(item2)
    output = value1, value2
    return output


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
