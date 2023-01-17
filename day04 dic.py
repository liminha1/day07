# dictionary
#
# students = {'name' : '김인하', 'age': 23, 'eyes': [0.9, 1.1]}
# # for dic in students.keys()
# # for dic in students:
# # for dic in students.values()
# for dic, vel in students.items():
#     print(f'{dic} : {vel}')
# print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end = ' ')
# print(f'시력은 좌: {students["eyes"][0]}, 우: {students["eyes"][1]}')
import random

# alcohol_foods = {
#     '맥주' : '치킨',
#     '소주' : '골뱅이소면',
#     '위스키' : '치즈',
#     '고량주' : '짬뽕'
# }
alcohol_foods = dict(맥주 = '치킨', 소주 = '골뱅이 소면', 위스키 = '치즈', 고량주 = '짬뽕')


alcohol_list = list(alcohol_foods) # extract keys
food_list = [food for food in alcohol_foods.values()]

for food in enumerate(food_list):
    print(food)

print(alcohol_list, food_list)
while True:
    alcohol = int(input(f'술을 선택하세요 \n1) {alcohol_list[0]} \n2) {alcohol_list[1]} \n3) {alcohol_list[2]} \n4) {alcohol_list[3]} \n5) 계산\n'
                        f'6) 술, 안주 아무거나\n7) 술 아무거나 - 해당 추천 안주\n8) 아무거나\n'))
    if alcohol == 5:
        print('다음에 또 오세요~')
        break
    elif alcohol == 1:
        print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다.')
    elif alcohol == 2:
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다.')
    elif alcohol == 3:
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다.')
    elif alcohol == 4:
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다.')
    elif alcohol == 6:
        print(f'무작위로 뽑은 술은 {alcohol_list[random.randint(0,3)]}입니다. 무작위로 뽑은 안주는 {alcohol_foods[alcohol_list[random.randint(0,3)]]}입니다.')
    elif alcohol == 7:
        a = random.randint(0,3)
        print(f'무작위로 뽑은 술은 {alcohol_list[a]}입니다. 추천하는 안주는 {alcohol_foods[alcohol_list[a]]}입니다.')
    elif alcohol == 8:
        print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다.')
    else:
        print('해당 숫자를 입력해 주세요.')