from asyncio import tasks
import random
from time import sleep


class Stack:
    def __init__(self):
        self.__stack_list = []

    @property
    def data(self):
        return self.__stack_list

    def push(self, value):
        if not str(value).isnumeric():
            raise ValueError ('nenomer')
        elif value > 50:
            print('1_c')
            sleep(1)
        elif value <=50:
            print('2_c')
            sleep(2)
        self.__stack_list.append(int(value))


    def pop(self):
        try:
            value = self.__stack_list[-1]
        except IndexError: 
            print('nerabotaet')
        del self.__stack_list[-1]
        return value
         

    def __str__(self) -> str:
        return str(self.__stack_list)




stack_1 = Stack()
stack_2 = Stack()


for i in range(random.randint(1, 5)):
    value = random.randint(1, 100)
    stack_1.push(value)


# stack_2.push(12)
# stack_2.push('g')


for i in range(random.randint(1, 5)):
    value = random.randint(1, 100)
    stack_2.push(value)

print(stack_1)
print(stack_2)

for i in range(random.randint(1, 5)):
    stack_1.pop()
    print(stack_1)


#_____________________________________________________________________


import asyncio
from asyncio.tasks import create_task

class AsyncStack(Stack):
    def __init__(self):
        self.stack = []
    
    async def push(self, value):
        
        if value > 50:
            print('1_c')
            await asyncio.sleep(1)
        elif value <=50:
            print('5_c')
            await asyncio.sleep(5)
        self.stack.append(int(value))

    def pop(self):
        try:
            value = self.stack[-1]
        except IndexError: 
            print('nerabotaet')
        del self.stack[-1]
        return value
         

    def __str__(self) -> str:
        return str(self.stack)

stack = Stack
as_stack = AsyncStack()


numbers = (random.randint(1, 100) for i in range(random.randint(1, 10)))
   


loop = asyncio.get_event_loop()
tasks = [as_stack.push(number) for number in numbers]
loop.run_until_complete(asyncio.gather(*tasks))
print(as_stack)

for i in range(random.randint(1, 5)):
    as_stack.pop()
    print(as_stack)

           