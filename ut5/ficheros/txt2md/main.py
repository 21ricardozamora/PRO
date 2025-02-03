def run(input_path: str, output_path: str) -> None:
    f = open(input_path)
    tag = '#'
    tab = '\t'
    output_lines = []
    for line in f.readlines():
        num_tabs = line.count(tab) + 1
        line = line.strip()
        total_hashtags = tag * num_tabs
        output_lines.append(f'{total_hashtags} {line}')
    f.close()
    with open(output_path, 'w') as f:
        for line in output_lines:
            f.write(line + '\n')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
