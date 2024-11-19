def run(u: list, v: list) -> float | None:
    length_v = len(v)
    length_u = len(u)
    mult_result = 0
    dprod = 0
    for num_v, num_u in zip(v, u):
        if length_v != length_u:
            dprod = None
            break
        else:
            mult_result = num_v * num_u
            dprod += mult_result
    return dprod


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
