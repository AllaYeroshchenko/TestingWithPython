# -*- coding: utf-8 -*-

def test_del_contact(app):
    app.session.login("Admin", "secret")
    app.contact.delete_first_contact()
    app.session.logout()



