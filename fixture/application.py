from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project_helper import ProjectHelper
from fixture.james_helper import JamesHelper
from fixture.singup_helper import SingupHelper
from fixture.mail_helper import MailHelper
from fixture.soap_helper import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.singup = SingupHelper(self)
        self.email = MailHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.james = JamesHelper(self)
        self.soap = SoapHelper(self)



    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
