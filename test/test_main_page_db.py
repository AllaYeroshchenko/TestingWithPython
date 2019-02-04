from model.contact import Contact

def test_main_page_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip(), firstname=contact.firstname.strip(), address=contact.address, all_phones_from_home_page=contact.all_phones_from_home_page, all_emails=contact.all_emails)
    assert sorted(map(clean, contacts_from_home_page), key=Contact.id_or_max) == sorted(map(clean, contacts_from_db), key=Contact.id_or_max)


