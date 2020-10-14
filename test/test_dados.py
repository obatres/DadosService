def dados(numero):
    if numero>=1 and numero <=6:
        return True

def test_dados():
    assert dados(5)==True