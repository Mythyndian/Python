import random
# wczytuje stolice do slownika
def wczytaj():
    f = open('stolice.txt', encoding='utf-8')
    linie = f.readlines()
    panstwo_stolica = {}
    for line in linie:
        para = line.split(', ')
        panstwo = para[0]
        stolica = para[1].strip('\n')
        panstwo_stolica[panstwo] = stolica
    f.close()
    return panstwo_stolica
# aktualnie printuje na ekran arkusz i odpowiadajacy mu klucz
def generuj(slownik, n):
    for test in range(n):
        a = open('arkusz{numer}.txt'.format(numer=str(test+1)),'w+', encoding='utf-8')
        a.write('''
Imię i nazwisko:

Data:

Semestr:

                    Stolice - sprawdzian (Formularz {numer})
        '''.format(numer=str(test+1)))
        panstwa = list(slownik.keys())
        stolice = list(slownik.values())
        random.shuffle(panstwa)
        random.shuffle(stolice)
        correct = []
        for i in range(46):
            # pytania nie mogą się powtarzać!
            pytanie = random.choice(panstwa)
            panstwa.pop(panstwa.index(pytanie))
            # odpowiedzi nie mogą się powtarzać wewnątrz jednego pytania
            odp = []
            odp.append(slownik[pytanie])
            for k in range(3):
                tester = random.choice(stolice)
                while tester == slownik[pytanie] and tester in odp:
                    tester = random.choice(stolice)
                odp.append(tester)
            random.shuffle(odp)
            if odp[0] == slownik[pytanie]:
                correct.append('A')
            elif odp[1] == slownik[pytanie]:
                correct.append('B')
            elif odp[2] == slownik[pytanie]:
                correct.append('C')
            elif odp[3] == slownik[pytanie]:
                correct.append('D')
            t = [i+1, pytanie, odp[0], odp[1], odp[2], odp[3]]

            a.write(
        '''


{0}.Jaką stolicę ma państwo {1}?
A.{2}
B.{3}
C.{4}
D.{5}'''.format(*t))

        a.close()
        o = open('klucz{numer}.txt'.format(numer=str(test+1)),'w+',encoding='utf-8')
        for i in range(46):
            o.write(str(i+1)+'.'+correct[i]+'\n')
        o.close()
generuj(wczytaj(), 10)
