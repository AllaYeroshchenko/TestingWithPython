from model.contact import Contact
import pytest
import random
import string

#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters+string.digits
#    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])

#testdata=[Contact(firstname="", lastname="", address="", nickname="", company="", title="", fax="", home="", mobile="",
#                  work="", email="")] + [
#       Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nikname", 10), title="title",
#                            company="company", address="address", home="home", mobile="111111", work="222222",
#                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000")
#    for i in range(5)
#]

testdata=[
    Contact(firstname="", lastname="", address="", nickname="", company="", title="", fax="", home="", mobile="", work="", email=""),
    Contact(firstname="name", lastname="kjkjhj", address="ghg", nickname="", company="", title="", fax="", home="", mobile="", work="", email="")
]