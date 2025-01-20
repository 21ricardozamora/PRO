def run(formula: list) -> bool:
    components1 = 1
    components2 = 2
    components3 = 3
    components4 = 4
    components5 = 5
    components6 = 6
    components7 = 7
    components8 = 8
    valid = True
    if components1 in formula and components2 in formula:
        valid = False
    elif components3 in formula and components4 in formula:
        valid = False
    elif components5 not in formula and components6 not in formula:
        valid = False
    elif components7 not in formula and components8 not in formula:
        valid = False
    return valid


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
