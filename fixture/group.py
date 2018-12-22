

class GroupHelper:

    def __init__(self, app):
        self.app=app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and (len(wd.find_elements_by_name("new")))>0):
            wd.find_element_by_link_text("groups").click()

    def to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and (len(wd.find_elements_by_name("new")))>0):
            wd.find_element_by_link_text("group page").click()

    def fill(self, group):
        wd = self.app.wd
        # fill group form
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.to_group_page()


    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # init group editing
        wd.find_element_by_name("edit").click()
        self.fill(group)
        # submit
        wd.find_element_by_name("update").click()
        self.to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.to_group_page()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))