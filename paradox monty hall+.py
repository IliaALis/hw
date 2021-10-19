import random

def get_not_matching(doors):
    for door in prize:
        if door not in doors:
            return door


prize = [1, 2, 3]
print('we have 3 doors before us')

choice_1 = random.choice(prize)
car = random.choice(prize)
print(car)
print('the first choice is door # {}'.format(choice_1))
goat_1_door = get_not_matching([choice_1, car])
print('the first goat is outside door # {}'.format(goat_1_door))
choice_2 = get_not_matching([choice_1, goat_1_door])
print('you can change your choice to door # {}'.format(choice_2))

change_choice = random.randint(1, 2)
if change_choice == 1:
    print('You do not change your choice')
    choice = choice_1
else:
    print('You change your choice')
    choice = choice_2

if choice == car:
    print('You win')
else:
    print('You lose')
