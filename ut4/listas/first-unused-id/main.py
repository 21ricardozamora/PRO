def run(ids: list) -> int:
    ONE = 1
    first_unused_id = 0
    sorted_ids = sorted(ids)
    if ONE not in sorted_ids:
        first_unused_id = ONE
    else:
        for _id in sorted_ids:
            if _id + ONE not in sorted_ids:
                first_unused_id = _id + ONE
                break
    return first_unused_id


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
