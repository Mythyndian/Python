class Account:

    def __int__(self, balance):
        self._balance = balance

    def pay(self):
        wplata = int(input('Podaj wysokosc wplaty: '))
        self._balance += wplata

    def take(self):
        wyplac = int(input('Podaj wysokosc wyplaty: '))
        if wyplac > self._balance:
            print('Niewystarczajac ilosc srodkow')
        else:
            self._balance -= wyplac

    def show_balance(self):
        return self._balance

    def __str__(self):
        return 'Na twoim koncie znajduje sie' + self._balance + 'zl'


balans = 2000
konto = Account(balans)
print(konto)
