def run(text: str) -> str:
    lengh_text = len(text)
    stext = text[1 : lengh_text - 1]
    return stext


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
