from selenium.webdriver.support.ui import Select
from model.contact import Contact
import time

class ContactHelper:

    def __init__(self, app):
        self.app=app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and (len(wd.find_elements_by_name("searchstring")))>0):
            wd.find_element_by_link_text("home").click()


    def fill(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)


    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #time.sleep(5)
        wd.switch_to_alert().accept()
        time.sleep(5)

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        #select first group
        #wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill(contact)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            firstname = element.find_element_by_xpath(".//td[3]").text
            lastname = element.find_element_by_xpath(".//td[2]").text
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts
