# -*- coding: utf-8 -*-
from model.contact import Contact

def test_del_contact(app):
    if app.contact.count()==0:
        app.contact.add(Contact(firstname="test", lastname="test", nickname="test", title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    old_contacts = app.contact.get_contact_list()
    #print(old_contacts)
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    #print(new_contacts)
    assert len(old_contacts)-1 == len(new_contacts)



