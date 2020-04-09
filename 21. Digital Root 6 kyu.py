# Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00

# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6


def alternative(number):
    while number > 9:
        number = sum([int(i) for i in str(number)])

    return number


def initial(n):
    number = int(n)
    num_sum = 0

    while True:
        for each in str(number):
            num_sum += int(each)
        if len(str(number)) == 1:
            result = num_sum
            break
        else:
            number = num_sum
            num_sum = 0

    return result


#print(digital_root(942))
print(alternative(942))
