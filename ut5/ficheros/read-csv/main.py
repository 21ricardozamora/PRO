def run(datafile: str) -> list:
    with open(datafile) as f:
        for line in range(3):
            print(f.readline)
            break
    return data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
