def run(current_pos: int, dice: int) -> int:
    final_pos = current_pos + 2 * (dice)
    return final_pos


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
