def binary(number):
    '''Converts decimal number to binary'''
    exponent = 0 #We're dealing with exponents of 2
    binary_number = 0 #The binary form of the number
    while number >= 2**exponent: #Finds the lowest power of 2
        exponent += 1 #the number is less than
    exponent -= 1
    for i in range(exponent + 1):
        if number - 2**exponent > -1: #If number contains power of 2
            binary_number += 10**exponent #Add that power of 10
            number -= 2**exponent #Take away that power of 2 from
            #number
        exponent -= 1 #Next lower exponent
    return binary_number

while True:
    number = input('Please input a decimal number: ')
    if number == 'q':
        break
    print('The binary is: ', binary(int(number)))
    