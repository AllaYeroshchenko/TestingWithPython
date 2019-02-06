import re
from model.contact import Contact

def test_main_page_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_home_page)):
       assert contacts_from_home_page[i].all_phones == merge_phones_like_on_home_page(contacts_from_db[i])
       assert contacts_from_home_page[i].all_emails == merge_emails_like_on_home_page(contacts_from_db[i])
       assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
       assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
       assert contacts_from_home_page[i].address == contacts_from_db[i].address

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_pfones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
        map(lambda x: clear(x),
            filter(lambda x: x is not None,
                   [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
            filter(lambda x: x is not None,
                   [contact.email, contact.email2, contact.email3])))
