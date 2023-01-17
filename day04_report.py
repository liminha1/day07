# 7.10
odd = []
for i in range(0,10,2):
    odd.append(i)
print(odd)
# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "someone better"
# 첫 번째
for i in range(0,3):
    start1[i] = start1[i].capitalize() + '! '
print(start1)
rhymes_list = []
for i in range(0,6):
    rhymes_list.append(list(rhymes[i]))
    rhymes_list[i][0] = rhymes_list[i][0].capitalize() + '!'
print(rhymes_list)
print(''.join(start1), end='')
print(rhymes_list[0][0])
# 두 번째
print(start2 + ' ', end ='')
print(rhymes_list[0][1] + '.')