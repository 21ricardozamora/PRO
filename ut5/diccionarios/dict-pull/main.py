def run(data: dict, target_keys: tuple) -> dict:
    pdata = {key: data.get(key) for key in data if key in target_keys}
    return pdata


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
