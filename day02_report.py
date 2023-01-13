import random

secret = random.randint(1,10)
guess = int(input('guess 값을 입력하세요: '))

if guess == secret:
    print('just right!')
elif guess < secret:
    print('too low!')
else:
    print('too high!')
print(f'secret은 {secret}입니다.')