import random


class Coin:
    def __init__(self):
        self.side = "orzel"

    def throw(self):
        self.side = random.choice(["orzel", "reszka"])

    def show_side(self):
        return self.side


zlotowa = Coin()
dwa_zlote = Coin()
piec_zloty = Coin()
wygrane = 0
przegrane = 0
for i in range(100):
    saldo = 0
    while saldo <= 20:
        zlotowa.throw()
        print("+1" if zlotowa.show_side() == "orzel" else "")
        if zlotowa.show_side() == "orzel":
            saldo += 1
        dwa_zlote.throw()
        print("+2" if dwa_zlote.show_side() == "orzel" else "")
        if dwa_zlote.show_side() == "orzel":
            saldo += 2
        piec_zloty.throw()
        print("+5" if piec_zloty.show_side() == "orzel" else "")
        if piec_zloty.show_side() == "orzel":
            saldo += 5

    print(saldo)
    if saldo == 20:
        wygrane += 1
    else:
        przegrane += 1

print(f'Po 100 symulacjach gry wynik to {wygrane} do {przegrane}')
