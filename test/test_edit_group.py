# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.session.login("Admin", "secret")
    app.group.edit_first_group(Group("GroupEdit", "HeaderEdit", "footerEdit"))
    app.session.logout()