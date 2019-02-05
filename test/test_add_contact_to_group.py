from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    if len(db.get_group_list())==0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list())==0:
        app.contact.add(Contact(firstname="test", lastname="test", nickname="test", title="title",
                            company="company", address="address", home="home", mobile="111111", work="222222",
                            fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
    all_groups = db.get_group_list()
    group=random.choice(all_groups)
    all_contacts = db.get_contact_list()
    contact=random.choice(all_contacts)
    app.contact.add_contact_to_group(group.id, contact)
    l=db.get_contacts_in_group(group)
    for item in l:
        print(item)
    print(len(l))
    assert db.is_contact_in_group(group, contact)==True