# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count()==0:
        app.contact.add(Contact(firstname="test", lastname="test", nickname="test", title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    old_contacts = app.contact.get_contact_list()
    contact=Contact(firstname="Alla1", lastname="Yeroshchenko1", nickname="Alochk1", title="title1",
                            company="company1", address="address1", home="home1", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000")
    index = randrange(len(old_contacts))
    contact.id=old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)