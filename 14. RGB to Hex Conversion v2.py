# better and more clever solutions:


# Solution 1
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))


# Solution 2
def rgb_2(r, g, b):
    round_f = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round_f(r), round_f(g), round_f(b))
