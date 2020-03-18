class TV:
    def __init__(self):
        self.volume = 0
        self.chanel = 0

    def change_chanel(self):
        while True:
            chanel = int(input('Input channel: '))
            if chanel in range(1, 101):
                self.chanel = chanel
                break

    def change_volume(self):
        while True:
            volume = int(input('Input volume: '))
            if volume in range(0, 101):
                self.volume = volume
                break

    def __str__(self):
        return f'Channel: {self.chanel}\nVolume: {self.volume}'


Samsung = TV()
Samsung.change_chanel()
print(Samsung)
Samsung.change_volume()
print(Samsung)
