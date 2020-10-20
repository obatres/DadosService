from random import randint as ran


def dados(numero):
    if numero >= 1 and numero <= 6:
        return True


def test_dados():
    a = ran(1, 6)
    assert dados(a) == True
