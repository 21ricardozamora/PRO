def run(text1: str, text2: str) -> int:
    dhamming = 0
    index = 0
    text1_size = len(text1)
    text2_size = len(text2)
    if text1_size != text2_size:
        dhamming = -1
    else:
        for char in range(text1_size):
            if text1[index] != text2[index]:
                dhamming += 1
            index += 1
    return dhamming


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
