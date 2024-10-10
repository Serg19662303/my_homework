import requests
import inspect
from pprint import pprint


class Test_intr:

    def __init__(self, num, word, bol):
        self.num = num
        self.word = word
        self.bol = bol

    def test_prnt(self):
        print(f'атрибуты: {self.bol}, {self.word}, {self.num}')


def introspection_info(obj):
    data_obj = {}
    attr, meth = [], []
    data_obj['name module'] = inspect.getmodule(obj)
    data_obj['type'] = type(obj)
    #if '__main__' in str(type(obj)):
    for attr_name in dir(obj):
        at = getattr(obj, attr_name)
        #if '__' not in str(attr_name):
        if 'method' in str(type(at)):
            meth.append(attr_name)
        else:
            attr.append(attr_name)
    data_obj['attributes'] = attr
    data_obj['methods'] = meth
    return data_obj

num = 345
word = 'слово'
bol = True
list_ = [num, word, bol]

test_obj = Test_intr(num, word, bol)
intr1 = introspection_info(test_obj)
intr2 = introspection_info(list_)
intr3 = introspection_info(num)

pprint(intr1)
print()
pprint(intr2)
print()
pprint(intr3)



