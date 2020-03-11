import random
class Die:

    def __init__(self, sides):
        self._value = None
        self._sides = sides

    def get_sides(self):
        return self._side

    def get_value(self):
        return self._value

    def roll(self):
        self._value = random.randrange(1, self._sides+1)


print('Game start')
print('Computer turn wait for you turn comupter is rolling the dies')

kostka = Die(6)
komputer = 0
gracz = 0

while True:
    # komputer
    if komputer < 21:
        kostka.roll()
        komputer += kostka.get_value()
        kostka.roll()
        komputer += kostka.get_value()
    if komputer == 21:
        print('Komputer wygral')
        break
    # gracz
    decyzja = input('Rzucasz dalej? (t/n): ')
    if decyzja == 't':
        if gracz < 21:
            kostka.roll()
            gracz += kostka.get_value()
            kostka.roll()
            gracz += kostka.get_value()
        if gracz == 21:
            print('Gratulacje pokonales maszyne')
            break
    else:
        break


print(f'Twoj wynik {gracz} wynik komputer {komputer}')