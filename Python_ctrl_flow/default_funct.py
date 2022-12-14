# default function
'''
def userName(userNamme, theSay):
    print(f'{theSay} {userNamme}')


userName("joseph", 'My name is')
'''


def ageRate(userAge, desiredAge):
    wishToLeave = desiredAge - userAge
    print(f'you will be {desiredAge} in {wishToLeave}')


userAge = int(input('How old are you?: '))
desiredAge = int(input('How old did you want to leave?: '))


ageRate(userAge, desiredAge)
