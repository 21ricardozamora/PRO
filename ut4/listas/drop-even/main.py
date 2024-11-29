def run(items: list) -> list:
    filter = []
    for index, char in enumerate(items):
        if index % 2 == 0:
            continue
        else:
            filter.append(char)
    return filter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
