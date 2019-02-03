# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list())==0:
        app.contact.add(Contact(firstname="test", lastname="test", nickname="test", title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    old_contacts = db.get_contact_list()
    contact_new=Contact(firstname="Alla1", lastname="Yeroshchenko1", nickname="Alochk1", title="title1",
                            company="company1", address="address1", home="home1", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000")
    contact=random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact_new, contact.id)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == contact_new.id:
            old_contacts[i] = contact_new
    assert len(old_contacts) == len(new_contacts)
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip(), firstname=contact.firstname.strip())
    if check_ui:
        assert sorted(map(clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
