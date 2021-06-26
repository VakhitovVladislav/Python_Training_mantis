from time import sleep


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.2/my_view_page.php")

    def create(self, project):
        wd = self.app.wd
        self.open_home_page()
        self.open_projects_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()


    def open_projects_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.2/manage_proj_create.php")
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text(u"Управление проектами").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'a[href ^= "manage_proj_edit_page.php?project_id={str(id)}"]').click()


    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.open_projects_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        self.open_projects_page()



