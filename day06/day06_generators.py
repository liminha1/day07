# print(sum(range(1,101)))
# def my_range(first = 0, last = 10, step = 1):
#     number = first
#     while number < last:
#         yield number
#         number += step
# ranger = my_range(1, 5)
# for x in ranger:
#     print(x)

def a():  # generator
    yield 1
    yield 2
    yield 3

def b():  # normal function
    return 1  # stop
    return 2
    return 3

print(a(),',', b())
c = a()
for i in c:
    print(i)
for i in c:
    print(i)

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
for thing in genobj:
    print(thing)
