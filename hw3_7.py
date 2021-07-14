

class Car:
    def __init__( self, model, year, brend, engine, color, price):

        self.brend = brend
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price
        

    def get_price(self):
        return f'The price is {self.price} of something'

    def get_complect(self):
        if self.color is 'red':
            new_price = self.price * 1.1
        else:
            new_price = self.price
        return f'This {self.color} color car price is {new_price}'
    
    def get_additional_options(self):
        icons_price = 20
        side_window_tinting_price = 100
        police_cap_price = 70
        new_price_ = self.price + icons_price + side_window_tinting_price + police_cap_price
        return f'Now this car price is {new_price_}'




byd_1 = Car(
            model = 'F_0',
            year = 2020,
            brend = 'Byd',
            engine = 2.1,
            color = 'red',
            price = 1000
    )

byd_2 = Car(
        model = 'F_0',
        year = 2020,
        brend = 'Byd',
        engine = 2.1,
        color = 'blue',
        price = 1000
) 




print(byd_1.get_additional_options())
print(byd_1.get_price())
print(byd_1.get_complect())

print(byd_2.get_additional_options())
print(byd_2.get_price())
print(byd_2.get_complect())