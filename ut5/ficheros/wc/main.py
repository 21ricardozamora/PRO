def run(input_path: str) -> tuple:
    f = open(input_path, 'r')
    num_lines = 0
    num_words = 0
    num_bytes = 0
    for line in f:
        num_lines += 1
        num_words += len(line.strip().split())
        num_bytes += len(line.encode('utf-8'))
    return num_lines, num_words, num_bytes


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
