# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group("Group1", "Header1", "footer1"))



def test_add_empty_group(app):
    app.group.create(Group("", "", ""))


