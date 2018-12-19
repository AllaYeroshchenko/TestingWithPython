# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Alla1", lastname="Yeroshchenko1", nickname="Alochk1", title="title1",
                            company="company1", address="address1", home="home1", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
