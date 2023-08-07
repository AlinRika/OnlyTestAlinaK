import time

from FormPage import Form


def test_by(browser):
    by_main_page = Form(browser)
    by_main_page.go_to_base_site()
    by_main_page.your_contacts()
    by_main_page.about_project()
    by_main_page.budget_about_us()
    by_main_page.captcha()
    by_main_page.sent_button()
    time.sleep(5)
    assert "Теперь Ваш проект в надежных руках" in by_main_page.get_successful_text()


