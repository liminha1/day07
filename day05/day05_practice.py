# # 딕셔너리
# signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
# print(len(signals))
# first = {'a': 'agony', 'b': 'bliss'}
# second = {'b':'bagels' ,'c': 'candy'}
# third = {'d': 'donuts'}
# print({**first, **second})
# print({**first, **third, **second})
#
# first.update(second)
# print(first)
# del first['a']
# print(first)
# print(first.pop('a', '해당 키가 존재하지 않습니다.'))
# print(first.pop('b'))
# first.clear()
# print(first)
# first = {'a': 'agony', 'b': 'bagels', 'd': 'donuts', 'c': 'candy'}
# print('a' in first)
# print('agony' in first)
#
# signals = first.copy()
# print(signals == first)
#
# import copy
# signals = {'a': ['agony', 1], 'b': 'bagels', 'd': 'donuts', 'c': 'candy'}
# first = copy.deepcopy(signals)
# print( signals == first )
# signals['a'][1] = 2
# print(first)
# print(signals)

accusation ={'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col.Mustard'}

for card, contents in accusation.items():
    print(f'Card {card} has the contents {contents}.')

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)