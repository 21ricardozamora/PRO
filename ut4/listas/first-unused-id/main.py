def run(ids: list) -> int:
    sorted_ids = sorted(ids)
    possible_id = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_id_index = possible_id[0]
    for id in sorted_ids:
        if possible_id_index not in sorted_ids:
            first_unused_id = possible_id_index
            break
        possible_id_index += 1
        if sorted_ids[-1] in possible_id:
            first_unused_id = possible_id_index
    return first_unused_id


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
