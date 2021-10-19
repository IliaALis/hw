import datetime

class Bar:

    def __init__(self):
        self.drinks = [
            {'name': 'vodka', 'quantity': 10, },
            {'name': 'rum', 'quantity': 2, },
            {'name': 'beer', 'quantity': 0, },
            {'name': 'wine', 'quantity': 20, },
        ]
        self.operations = []


    def get_drink(self, name, amount):
        for drink in self.drinks:
            if name in drink['name']:
                if drink['quantity'] > 0:
                    if drink['quantity'] >= amount:
                        drink['quantity'] -= amount
                        self.drinks
                        self.operations.append(self.operation(name, amount, date, 'sale'))
                        return "Here you are"
                    else:
                        rest = str(drink['quantity'])
                        return "we have only " + rest
                else:
                    return "It finished"
        else:
            return "better take vodka"


    def supply(self, name, amount):
        for drink in self.drinks:
            if name in drink['name']:
                drink['quantity'] += amount
                self.operations.append(self.operation(name, amount, date, 'arrival'))
                return self.operations
        else:
            new_drink = {
                'name': name,
                'quantity': amount,
            }
            self.operations.append(self.operation(name, amount, date, 'arrival'))
            self.drinks.append(new_drink)
            # return()


    def operation(self, name, amount, date, op_type):
        date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        operation_drink = {
            'name': name,
            'quantity': amount,
            'date': date,
            'type': op_type,
            }
        return operation_drink


bar = Bar()
date = datetime.datetime.now()
while True:

    print(bar.drinks)
    print("\nWe have: ")
    for drink in bar.drinks:
        if drink['quantity'] != 0:
            print(drink['name'])
    name = input('what do you want?\n')
    amount = input('how much?\n')
    op_type = 0
    if amount.isdigit():
        amount = int(amount)
    else:
        print('man, you too drunk')
        break
    print(bar.get_drink(name, amount))

    while True:
        if input('\nWill we buy the goods?(y/n)') == 'y':
            name = input("what to bring?\n")
            amount = int(input("how much to bring?\n"))
            bar.supply(name, amount)
        else:
            print(bar.operations)
            break

    if input('something else?(y/n)') == 'n':
        break
