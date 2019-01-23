# -*- coding: utf-8 -*-
from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[Group(id=None, name="", header="", footer="")] + [
    Group(random_string("name", 10), random_string("header", 15), random_string("footer", 20))
    for i in range(5)
]