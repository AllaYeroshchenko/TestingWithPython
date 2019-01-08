# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])

testdata=[Contact(firstname="", lastname="", address="", nickname="", company="", title="", fax="", home="", mobile="",
                  work="", email="")] + [
        Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nikname", 10), title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000")
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



