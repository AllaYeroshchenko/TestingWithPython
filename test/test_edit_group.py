# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list())==0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new=Group("GroupEdit", "HeaderEdit", "footerEdit")
    app.group.edit_group_by_id(group.id, group_new)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id==group_new.id:
            old_groups[i]=group_new
    assert len(old_groups) == len(new_groups)
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
