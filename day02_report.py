small = bool(int(input('it is small. True면 1, False면 0을 입력하시오. : ')))
green = bool(int(input('it is green. True면 1, False면 0을 입력하시오. : ')))

if small:
    if green:
        print('완두콩 입니다!')
    else:
        print('체리 입니다!')
else:
    if green:
        print('수박 입니다!')
    else:
        print('호박 입니다!')