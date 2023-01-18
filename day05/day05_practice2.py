# s= set((1,2,3))
# s.add(4)
# print(s)
# s.remove(4)
# print(s)
# furniture = set(('sofa', 'ottoman', 'table'))
# for piece in furniture:
#     print(piece)

# drinks = {
#     'martini' : {'vodka', 'vermouth'},
#     'black russian' : {'vodka', 'kahlua'},
#     'white russian' : {'cream', 'kahlua', 'vodka'},
#     'manhattan' : {'rye', 'vermouth', 'bitters'},
#     'screwdriver' : {'orange juice', 'vodka'}
# }
# for name, contents in drinks.items():
#     if 'vodka' in contents:
#         print(name)
# print('\n')
# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)
# print('\n')
# for name, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}:
#         print(name)
# print('\n')
# for name, contents in drinks.items():
#     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
#         print(name)
# print('\n')
# bruss = drinks['black russian']
# wruss = drinks['white russian']
# a = {1,2}
# b = {2,3}
# print(a & b)
# print(a.intersection(b))
# print( bruss & wruss )
# print( a | b )
# print(a.union(b))
# print(bruss|wruss)
# print( a-b )
# print(a.difference(b))
# print(bruss-wruss)
# print(wruss - bruss)
# print(a^b)
# print(a.symmetric_difference(b))
# print(bruss ^ wruss)
# print(a<=b)
# print(bruss<=wruss)
# print(bruss < wruss)

a_set = { number for number in range(1,6) if number % 3 == 1}
print(a_set)