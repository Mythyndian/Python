import pickle


class Smartphone:

    def __init__(self):
        self.__maufacturer = None
        self.__model = None
        self.__price = None
    
    def set_manufacturer(self):
        self.__maufacturer = input('Input manufacturer: ')

    def set_model(self):
        self.__model = input('Input manufacturer: ')

    def set_price(self):
        self.__price = input('Input price: ')

    def get_manufacturer(self):
        print(f'Manufacturer: {self.__maufacturer}')

    def get_model(self):
        print(f'Model: {self.__model}')

    def get_price(self):
        print(f'Price: {self.__price}')

    def __str__(self):
        return f'Manufacturer: {self.__maufacturer} \nModel: {self.__model} \nPrice: {self.__price}'


Samsung = Smartphone()
Samsung.set_manufacturer()
Samsung.set_model()
Samsung.set_price()

print(Samsung)
file = open('phones.dat', 'wb')
pickle.dump(Samsung, file)
file.close()

file = open('phones.dat', 'rb')
print(pickle.load(file))
file.close()
