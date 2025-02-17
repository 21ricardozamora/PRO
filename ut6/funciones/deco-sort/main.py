# TODO


@sort(asc=False)
def run(values: list) -> list:
    return [v for v in values if v % 2 == 0]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
