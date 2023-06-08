# TDD - Test Driven Development

def greet(name, isEnemy):
    if not isEnemy:
        return f'Hello {name}, How are you?'
    else:
        return f'Hello {name}! I wil l kill you, bastard!'


def eat_burgers(count):
    if count<=3:
        return 'Mmm, that was excellent!'
    else:
        return 'Oh, I overate!'
    
def can_fly(person):
    if person.lower() == 'batmann':
        return True
    else: return False