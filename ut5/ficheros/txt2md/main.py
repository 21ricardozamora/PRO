def run(input_path: str, output_path: str) -> None:
    f = open(input_path, 'r')
    f_outpath = open(output_path, 'w')
    for line in f:
        line = line.replace('    ', '#')
    f_outpath.write(line + '\n')
    f_outpath.close()


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
