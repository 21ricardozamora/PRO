def mcount(values: tuple[int], target_num: int) -> int:
    """Calculate how many times target_num is in values.
    :param values: a tuple with integers
    :type values: tuple
    :param target_num: the number what we are searching
    :type target_num: int
    :type counter: int
    :return: number of times target_num is in values
    :rtype:int
    """
    counter = 0
    for value in values:
        if value == target_num:
            counter += 1
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(mcount)
