# def print_more(required1, required2, *args):
#     print('Need this one: ', required1)
#     print('Need this one too: ', required2)
#     print('all the rest: ', args)
# print_more('cap', 'gloves', 'scarf', 'moncle', 'mustache wax')


# import random
# def calculate_fee(*args):
#     '''
#     놀이공원 요금 계산 프로그램
#     :param arg:  ages
#     :return:  지불할 총 입장료
#     '''
#     total = 0
#     for age in args:
#         if 10 <= age:  # adult
#             total = total + 10000
#         else:
#             total = total + 3000
#     return total
#
# print(calculate_fee(20, 20, 25))
# print(calculate_fee(45, 43, 10, 7))

# import random
# def calculate_fee(args)-> list:
#     '''
#     놀이공원 요금 계산 프로그램
#     :param arg:  ages in list
#     :return:  [전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료]
#     '''
#     total = 0
#     adults = 0
#     kids = 0
#     for age in args:
#         if 10 <= age:  # adult
#             total = total + 10000
#             adults += 1
#         else:
#             total = total + 3000
#             kids += 1
#     return {len(args), adults, kids, total}
#
# no_of_visitor = int(input('몇 분이서 오셨나요? '))
# ages = [random.randint(1,60) for age in range(no_of_visitor)]
# results = calculate_fee(ages)
# print(f'{results[0]}명 방문 하셨고, 어른 {results[1]}명, 아이 {results[2]}명 총 요금은 {results[-1]}원 입니다.')

# 5분 방문하셨고 어른 2명 아이 3명 총 요금은 10000원 입니다.

# print(calculate_fee(20, 20, 25))
# print(calculate_fee(45, 43, 10, 7))

import random
def calculate_fee(args)-> dict:
    '''
    놀이공원 요금 계산 프로그램
    :param arg:  ages in dictionary
    :return:  {'no_of_ people' : 전체 인원 수, 'no_of_adult': 어른 수, 'no_ of_kid' : 아이 수, 'total_fee': 입장료}
    '''
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 10 <= age:  # adult
            total = total + 10000
            adults += 1
        else:
            total = total + 3000
            kids += 1
    return {'no_of_ people' : len(args), 'no_of_adult': adults, 'no_ of_kid' : kids, 'total_fee': total}

no_of_visitor = int(input('몇 분이서 오셨나요? '))
ages = [random.randint(1,60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(f'{results["no_of_ people"]}명 방문 하셨고, 어른 {results["no_of_adult"]}명, 아이 {results["no_ of_kid"]}명 총 요금은 {results["total_fee"]}원 입니다.')