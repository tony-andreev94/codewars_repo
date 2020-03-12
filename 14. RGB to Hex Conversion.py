# The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.
# The following are examples of expected output values:
# Example:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255

    if g < 0:
        g = 0
    elif g > 255:
        g = 255

    if b < 0:
        b = 0
    elif b > 255:
        b = 255

    hex_string = ""
    if r == 0:
        hex_string += '00'
    elif 0 < r < 10:
        hex_string += '0'
        hex_string += str(r)
    else:
        hex_string += hex(r)[2:].upper()

    if g == 0:
        hex_string += '00'
    elif 0 < g < 10:
        hex_string += '0'
        hex_string += str(g)
    else:
        hex_string += hex(g)[2:].upper()

    if b == 0:
        hex_string += '00'
    elif 0 < b < 10:
        hex_string += '0'
        hex_string += str(b)
    else:
        hex_string += hex(b)[2:].upper()

    return hex_string


red = int(input())
green = int(input())
blue = int(input())

print(rgb(red, green, blue))
