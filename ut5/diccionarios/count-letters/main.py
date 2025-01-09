def run(text: str) -> dict:
    counter = {}
    for item in text:
        if item not in counter:
            repeat_times = 0
            repeat_times += 1
        else:
            repeat_item = counter.get(item) + 1
            repeat_times = repeat_item
        counter[item] = repeat_times
    return counter


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
