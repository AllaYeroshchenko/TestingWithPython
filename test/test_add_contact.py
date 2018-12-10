# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login("Admin", "secret")
    app.add_contact(Contact(firstname="Alla", lastname="Yeroshchenko", nickname="Alochka", title="title",
                                         company="company", address="address", home="home", mobile="111111", work="222222",
                                         fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    app.session.logout()


