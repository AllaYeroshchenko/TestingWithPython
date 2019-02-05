from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l=db.get_contacts_not_in_group(Group(id="279"))
    for item in l:
        print(item)
    print(len(l))
    d=db.is_contact_in_group(Group(id="279"), Contact(id="270"))
    print(d)
finally:
    pass #db.destroy()