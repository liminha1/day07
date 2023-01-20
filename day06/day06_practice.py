# def commentary(color):
#     if color == 'red':
#         return "It's a tomato."
#     elif color == 'green':
#         return "it's a green pepper."
#     elif color == 'bee purple':
#         return "I don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color " + color + "."
# comment = commentary('blue')
# print(comment)
#
# thing = None
# if thing :
#     print("It's some thing.")
# else:
#     print("It's no thing.")
#
# def whatis(thing):
#     if thing is None:
#         print(thing, "is None")
#     elif thing:
#         print(thing, "is True")
#     else:
#         print(thing, "is False")
#
# whatis(None)
# whatis(True)
# whatis(False)
# whatis(0)
# whatis(0.0)
# whatis('')
# whatis('''''')
# whatis(())
# whatis([])
# whatis({})
# whatis(set())
# whatis(0.00001)
# whatis([0])
# whatis([''])
# whatis(' ')

# def menu(wine, entree, dessert):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}
#
# a = menu('chardonnay', 'chicken', 'cake')
# print(a)
#
# def menu(wine, entree, dessert = 'pudding'):
#     return {'wine':wine, 'entree':entree, 'dessert': dessert}
# print(menu('chardonnay', 'chicken'))
#
# def buggy(arg, result = []):
#     result.append(arg)
#     print(result)
#
# buggy('a')
# buggy('b', ['b'])
# buggy('b')

def print_args(*args):
    print('Positional tuple: ', args)
print_args()
print_args(3, 2, 1, 'wail!', 'uh...')



