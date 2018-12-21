# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group("GroupEdit", "HeaderEdit", "footerEdit"))
