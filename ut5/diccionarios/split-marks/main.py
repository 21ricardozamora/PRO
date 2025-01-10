def run(marks: dict) -> tuple:
    passed = {name.upper(): marks.get(name) for name in marks if marks.get(name) >= 5}
    failed = {name.lower(): marks.get(name) for name in marks if marks.get(name) < 5}
    return passed, failed


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
