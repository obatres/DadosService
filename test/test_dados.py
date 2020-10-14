from random import randrange as ran

def dados(numero):
    if numero>=1 and numero <=6:
        return True

def test_dados():
    a  = ran(6)
    assert dados(a)==True