# 6.3
guess_me = 5
for number in range(0,10):
    if guess_me > number:
        print('too low')
    elif guess_me == number:
        print('found it')
        break
    else:
        print('opp')
        break