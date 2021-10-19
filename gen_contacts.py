import random
import names


prefixes = ['055', '066', '095', '099',]

def get_random_phone():
    pref = random.choice(prefixes)
    rand_num = random.randint(0, 9999999)
    return (pref+'{:07d}'.format (rand_num))



for x in range(10):
    first_name =  names.get_first_name
    last_name = names.get_last_name
    phone = get_random_phone()
    email = first_name.lower() + '.' + last_name.lower() + '@gmail.com'


    print(first_name, last_name, phone)
    cure.execute (insert )
