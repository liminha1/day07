# function

def isprime(n):
    '''
    매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param n: integer number
    :return: true ot false
    '''
    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True

help(isprime)
# print(isprime(119))

start = int(input("input start : "))
end = int(input("input end : "))

if end < start:
    start, end = end, start

for i in range(start, end+1):
    if isprime(i):
        print(i,end = ' ')

    # if i <= 1:
    #     continue
    # for k in range(2, i):
    #     if i % k == 0:
    #         break
    # else:
    #     print(i, end = ' ')
