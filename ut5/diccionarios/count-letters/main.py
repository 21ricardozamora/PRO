def run(text: str) -> dict:
    counter = {}
    repeat_times = 0
    letters = []
    for item in text:
        if item not in letters:
            letters.append(item)
            repeat_times += 1
        else:
            letters.append(item)
        counter[letters] = repeat_times
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
