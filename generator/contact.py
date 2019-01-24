# -*- coding: utf-8 -*-
from model.contact import Contact
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
f="data/contacts.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])

testdata=[Contact(firstname="", lastname="", address="", nickname="", company="", title="", fax="", home="", mobile="",
                  work="", email="")] + [
        Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nikname", 10), title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000")
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fw:
    jsonpickle.set_encoder_options("json", indent=2)
    fw.write(jsonpickle.encode(testdata))
