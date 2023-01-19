def do_nothing():
    pass
def make_a_sound():
    print('quack')
def agree():
    return True
if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

def echo(anything):
    return anything + ' ' + anything

print(echo('Rumplestiltskin'))

def commentary(color):
    if