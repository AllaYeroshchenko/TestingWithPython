# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_add_group(app):
    time.sleep(5)
    app.session.login("Admin", "secret")
    app.group.create(Group("Group1", "Header1", "footer1"))
    app.session.logout()


def test_add_empty_group(app):
    time.sleep(5)
    app.session.login("Admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()

