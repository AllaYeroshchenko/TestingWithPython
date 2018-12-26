# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count()==0:
        app.contact.add(Contact(firstname="test", lastname="test", nickname="test", title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    old_groups = app.group.get_group_list()
    app.contact.edit_first_contact(Contact(firstname="Alla1", lastname="Yeroshchenko1", nickname="Alochk1", title="title1",
                            company="company1", address="address1", home="home1", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)