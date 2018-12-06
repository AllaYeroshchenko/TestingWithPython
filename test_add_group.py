# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest

class UntitledTestCase2(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "Admin", "secret")
        self.create_group(wd, Group("Group1", "Header1", "footer1"))
        self.to_group_page(wd)
        self.logout(wd)

    def test_untitled_test_case_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "Admin", "secret")
        self.create_group(wd, Group("", "", ""))
        self.to_group_page(wd)
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

    def login(self, wd, login, password):
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open homepage
        wd.get("http://localhost/addressbook/group.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
