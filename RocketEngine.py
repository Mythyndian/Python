class RocketEngine:
    count = 0
    all_power = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.working = False
        RocketEngine.count += 1

    def start(self):
        if not self.working:
            self.working = True
            print(f'Engaging launch of {self.name} module')
        RocketEngine.all_power += self.power

    def stop(self):
        if self.working:
            RocketEngine.all_power -= self.power
            self.working = False

    def __str__(self):
        return f'Name: {self.name}\nPower: {self.power}\nWorking: {self.working}'

    def __del__(self):
        RocketEngine.count -= 1
        print(f'Disengaging module {self.name} ')

    @staticmethod
    def status():
        print(f'Count: {RocketEngine.count}\nAll power: {RocketEngine.all_power}')
