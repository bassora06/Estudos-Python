from typing import Any


class CallMe():
    def __init__(self, number):
        self.number = number

    def __call__(self, *args, **kwargs):
        print('Ligando', self.number)
        return sum(args)
    

call1 = CallMe(989835005)
print(call1(12, 12, 12, 11))