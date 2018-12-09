# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.login(wd, "Admin", "secret")
        self.create_group(wd, Group("Group1", "Header1", "footer1"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, "Admin", "secret")
        self.create_group(wd, Group("", "", ""))
        self.logout(wd)


    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def to_group_page(self, wd):
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.to_group_page(wd)


    def login(self, wd, login, password):
        # login
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open homepage
        wd.get("http://localhost/addressbook/group.php")

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
