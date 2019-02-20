# -*- coding: utf-8 -*-
from model.group import Group
#import pytest
#import allure_pytest
#from data.groups import testdata



#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, json_groups, check_ui):
    group=json_groups
 #   with allure_pytest.step('Given a group list'):
    old_groups = db.get_group_list()
 #   with allure_pytest.step('When I add a group %s to the list' % group):
    app.group.create(group)
  #  with allure_pytest.step('Then the new group list is equal to the old list with the added group'):
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




