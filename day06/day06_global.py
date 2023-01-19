# g =1
#
# def change_print_global():
#     """
#     This is the amazing function.
#     want to see it again?
#     :return:
#     """
#     global g
#     print(g)
#     g = 2
#     print(g)
#
# change_print_global()
# print(g)
# print(globals())
# print(__name__)
# print(__doc__)
# print(__package__)
# print(__loader__)
#
# def factorial_iter(n):
#     """
#     반복문을 사용한 팩토리얼 함수
#     :param n: n!
#     :return: iterger 팩토리얼 계산 결과 값
#     """
#     result = 1
#     for k in range(1, n+1):
#         result = result * k
#     return result
#
# def factorial_recu(n):
#     """
#     재귀 함수를 사용한 팩토리얼 계산 결과 값
#     :param n: n!
#     :return: 자기 자신을 호출 또는 1
#     """
#     if n == 1:  # 끝나는 조건
#         return 1
#     else:
#         return factorial_recu(n-1) * n
#
#
# print(factorial_recu(5))
# print(factorial_iter(5))

# def div_calc(a,b):
#     """
#     나누기 함수
#     :param a: 분자
#     :param b: 분모
#     :return: 계산 결과
#     """
#     return a / b

# print(div_calc(15, 3))
# print(div_calc(7, 0))

try :
    expr = input('분자 분모 입력 (띄어쓰기로 구분): ').split()
    print(int(expr[0]) / int(expr[1]))
# value error
# zeroDivisionError
except ValueError as err:
    print(f'숫자를 입력해주세요. ({err})')
except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다. ({err})')
except IndexError as err:
    print(f'입력 값의 범위에 문제가 있습니다. ({err})')
except Exception as other:
    print(f'예외 발생! ({other})')
else:  # 예외가 발생하지 않았을 떄
    print('프로그램 정상', end = ' ')
finally:  # 예외 발생 여부와 상관 없이 무조건 실행
    print('종료')