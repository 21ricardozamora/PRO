def run(items: dict) -> dict:
    fitems = {}
    keys_fitems = ''
    for item in items.keys():
        keys_fitems = item
        keys_fitems = keys_fitems.strip().replace(' ', '')
        fitems[keys_fitems] = items.get(item)
    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
