# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment,
# so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones
# -- every time you press the button it sends you an array of one-letter strings representing directions to walk
# (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block in a direction and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes
# (you don't want to be early or late!) and will, of course, return you to your starting point.
# Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction letters
# ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


# my initial solution
def is_valid_walk(walk):
    #determine if walk is valid
    x = 0
    y = 0
    if len(walk) == 10:
        for each_item in walk:
            if each_item == 'n':
                y += 1
            elif each_item == 's':
                y -= 1
            elif each_item == 'e':
                x += 1
            elif each_item == 'w':
                x -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False

    else:
        return False


# better alternative solution
def is_a_valid_walk(walk):
    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
        return True
    else:
        return False


walk_input = input().split(', ')
print(is_valid_walk(walk_input))