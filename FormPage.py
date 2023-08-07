from selenium.webdriver.common.by import By
from BaseApp import BasePage


class FormLocators:
    locator_name = (By.XPATH, "//input[@name='name']")
    locator_email = (By.XPATH, "//input[@name='email']")
    locator_phone = (By.XPATH, "//input[@name='phone']")
    locator_company = (By.XPATH, "//input[@name='company']")
    locator_about_project = (By.XPATH, "//form[@class='sc-60972c5f-5 fUfKIm']/div[2]/div/label[4]")
    locator_text_about_project = (By.XPATH, "//textarea[@placeholder='Расскажите о вашем проекте']")
    locator_budget = (By.XPATH, "//form[@class='sc-60972c5f-5 fUfKIm']/div[3]/div/label[2]")
    locator_about_us = (By.XPATH, "//form[@class='sc-60972c5f-5 fUfKIm']/div[4]/div/label[1]")
    locator_captcha = (By.XPATH, "//label[@id='recaptcha-anchor-label']")
    locator_sent_button = (By.XPATH, "//form[@class='sc-60972c5f-5 fUfKIm']/div[6]/button")
    locator_successful_text = (By.XPATH, "//p[@class='sc-fa59ff4e-1 LfAir']")


class Form(BasePage):

    def your_contacts(self):
        name = self.find_element(FormLocators.locator_name)
        name.send_keys('Иван')
        email = self.find_element(FormLocators.locator_email)
        email.send_keys('test@test.ru')
        phone = self.find_element(FormLocators.locator_phone)
        phone.click()
        phone.send_keys('9999999999')
        company = self.find_element(FormLocators.locator_company)
        company.send_keys('Test Company')

    def about_project(self):
        text_about_project = self.find_element(FormLocators.locator_text_about_project)
        self.actions.move_to_element(text_about_project).perform()
        text_about_project.send_keys('Проект - "Я молодец"')
        about_project = self.find_element(FormLocators.locator_about_project)
        about_project.click()

    def budget_about_us(self):
        budget = self.find_element(FormLocators.locator_budget)
        self.actions.move_to_element(budget).perform()
        budget.click()
        about_us = self.find_element(FormLocators.locator_about_us)
        self.actions.move_to_element(about_us).perform()
        about_us.click()

    def captcha(self):
        about_us = self.find_element(FormLocators.locator_about_us)
        sent_button = self.find_element(FormLocators.locator_sent_button)
        self.actions.move_to_element(sent_button).perform()
        location_about_us = about_us.location
        location_sent_button = sent_button.location
        x = (location_about_us['x'] + location_sent_button['x']) // 2
        y = (location_about_us['y'] + location_sent_button['y']) // 2
        self.actions.reset_actions()
        self.actions.move_by_offset(x, y + 10).click().perform()

    def sent_button(self):
        sent_button = self.find_element(FormLocators.locator_sent_button)
        sent_button.click()

    def get_successful_text(self):
        successful_text = self.find_element(FormLocators.locator_successful_text).text
        return successful_text

