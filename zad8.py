class Pet:

    def __init__(self):
        self.hunger = 0
        self.tiredness = 0
        while True:
            name = input('Input name of your pet (min. 3 characters) : ')
            if len(name) > 3:
                self.name = name
                break

    @property
    def mood(self):
        if self.hunger + self.tiredness < 5:
            return 'Happy'

        if 5 < self.hunger + self.tiredness < 10:
            return 'Pleased'

        if 11 < self.hunger + self.tiredness < 15:
            return 'Angry'

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    def eat(self, food=4):
        if self.hunger >= 4:
            self.hunger -= food
            self._passage_of_time()
        else:
            print('Your pet don\'t want to eat')

    def play(self, fun=4):
        if self.tiredness >= 4:
            self.tiredness -= 4
            self._passage_of_time()
        else:
            print('Your pet don\'t want to play')

    def talk(self):
        print(f'Your {self.name} is {self.mood}')
        self._passage_of_time()

    def __str__(self):
        return f'Name: {self.name}\nTiredness: {self.tiredness}\nHunger: {self.hunger}\nMood: {self.mood}'


def main():
    zwierzatko = Pet()
    while True:
        print('1.Talk (check on mood)')
        print('2.Give something to eat')
        print('3.Play')
        print('4.Status')
        print('5.Leave')
        decide = int(input('What are you going to do? (Pick 1-5): '))
        if 1 <= decide <= 5:
            if decide == 1:
                zwierzatko.talk()
            elif decide == 2:
                food = int(input('How much food? : '))
                zwierzatko.eat(food)
            elif decide == 3:
                fun = int(input('How long do you wanna play for?'))
                zwierzatko.play(fun)
            elif decide == 4:
                print(zwierzatko)
            elif decide == 5:
                break
        else:
            print('You entered wrong number try again :)')


main()
