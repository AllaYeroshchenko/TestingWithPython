# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group(Group("GroupEdit", "HeaderEdit", "footerEdit"))
