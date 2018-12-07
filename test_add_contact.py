# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.add_contact(driver, Contact(firstname="Alla", lastname="Yeroshchenko", nickname="Alochka", title="title",
                                         company="company", address="address", home="home", mobile="111111", work="222222",
                                         fax="333333", email="yeroshchenko@gmail.com", bday="17", bmonth="July", byear="2000"))
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def add_contact(self, driver, contact):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work)
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, driver):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
