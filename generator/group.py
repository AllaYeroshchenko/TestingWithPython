# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args=getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=6
f="data/groups.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata=[Group(id=None, name="", header="", footer="")] + [
    Group(random_string("name", 10), random_string("header", 15), random_string("footer", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fw:
    jsonpickle.set_encoder_options("json", indent=2)
    fw.write(jsonpickle.encode(testdata))
