# -*- coding: utf-8 -*-
from application import Application
from contact import Contact
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login("Admin", "secret")
        self.app.add_contact(Contact(firstname="Alla", lastname="Yeroshchenko", nickname="Alochka", title="title",
                                         company="company", address="address", home="home", mobile="111111", work="222222",
                                         fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
