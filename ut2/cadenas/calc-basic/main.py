def run():
    number1 = int(input('Enter a number: '))
    number2 = int(input('Enter a number: '))
    result_add = number1 + number2
    result_substract = number1 - number2
    result_mult = number1 * number2
    result_div = number1 // number2
    print(number1, '+', number2, '=', result_add, sep='')
    print(number1, '-', number2, '=', result_substract, sep='')
    print(number1, '*', number2, '=', result_mult, sep='')
    print(number1, '/', number2, '=', result_div, sep='')


asdasd

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
