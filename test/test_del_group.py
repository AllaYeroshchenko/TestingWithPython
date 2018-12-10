# -*- coding: utf-8 -*-
from model.group import Group

def test_del_group(app):
    app.session.login("Admin", "secret")
    app.group.delete_first_group()
    app.session.logout()