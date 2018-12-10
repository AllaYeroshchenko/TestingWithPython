# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login("Admin", "secret")
    app.create_group(Group("Group1", "Header1", "footer1"))
    app.logout()

def test_add_empty_group(app):
    app.login("Admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()
