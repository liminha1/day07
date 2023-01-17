#list
# scores = ('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1], scores[2])

# big_bang = ['지디', '태양', '탑', '대성', '승리']
# exo = ['백현', '첸']
# # big_bang.append('인하')
# big_bang.insert(1, '인하')
# # print(big_bang * 2)
# # exo.extend(big_bang)
# # exo = exo + big_bang
# exo.append(big_bang)
# # print(exo[2][2])  #태양
# # print(exo[-1][-4])  #태양
# print(exo[2].pop())  #승리 pop
# print(exo[2].pop(3))  #탑 pop
# del exo[2][-1]  #대성 del
# exo[2].remove('인하')  #인하 remove
# exo.clear()
# print(exo)

#list
# primes = [2, 19, 3.0, 5, 7, 11]
# # primes_sorted = sorted(primes)
# primes.sort()
# print(primes)
# # print(primes_sorted)

# # mixed = [6,4,5,'A',7,'트와이스','B','b','마마무'] # 에러
# mixed = ['6','4','5','A','7','트와이스','B','b','마마무']
# # mixed.sort()
# mixed.sort(reverse = True)
# print(mixed)

thing = ["mozzarella", "cinderella", "salmonella"]
thing[1] = thing[1].title()
print(thing)
thing[0] = thing[0].upper()
print(thing)
thing.pop()
print(thing)

