# 5.2
# q = ['q1', 'q2', 'q3']
# a = ['a1', 'a2', 'a3']
#
# for i in range(0,3):
#  print(f'{q[i]}? \n {a[i]}')

# 5.4
letter = """
    Dear {salutation} {name},
    
    Thank you for your letter. We are sorry that 
    our {product} {verbed} in your {room}.
    Pleas note that it should never be used in a {room},
    especially near any {animals}.
    
    Send us your reciept and {amount} for shipping and handling.
    We will send you another {product} that, in our tests, is
    {percent}% less likely to have {verbed}.
    
    Thank you for your support.
    Sincerely,
    {spokesman}
    {job_title}
"""
# 5.5
print(letter.format(salutation = 'A', name = 'jun', product = 'C',
                    verbed = 'D', room = 'E', animals = 'F'
                    , amount = 'G', percent = '100',
                    spokesman = 'H', job_title = 'I'))