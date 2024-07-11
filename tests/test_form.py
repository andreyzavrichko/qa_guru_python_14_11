import allure
from allure_commons.types import Severity

from pages.form_page import RegistrationForm


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Аркадий Укупник")
@allure.feature("Регистрация")
@allure.story("Проверка заполнения формы регистрации")
def test_complete_todo(setup_browser):
    registration_form = RegistrationForm()
    with allure.step("Открываем главную страницу"):
        registration_form.open()
    with allure.step("Заполняем форму"):
        registration_form.type_first_name('Alex')
        registration_form.type_last_name('Smirnov')
        registration_form.type_email('alex.smirnov@gmail.com')
        registration_form.click_gender()
        registration_form.type_phone('5648798798')
        registration_form.type_birthday()
        registration_form.type_subjects('Computer Science')
        registration_form.click_hobbies()
        registration_form.upload_photo('img.png')
        registration_form.type_address('Moscow, Manoilov Street, 64')
        registration_form.type_state('NCR')
        registration_form.type_city('Gurgaon')
        registration_form.press_submit()
    with allure.step("Проверяем заголовок"):
        registration_form.should_text('Thanks for submitting the form')
    with allure.step("Проверяем форму"):
        registration_form.should_exact_text('Alex Smirnov',
                                            'alex.smirnov@gmail.com',
                                            'Male',
                                            '5648798798',
                                            '15 May,2014',
                                            'Computer Science',
                                            'Sports',
                                            'img.png',
                                            'Moscow, Manoilov Street, 64',
                                            'NCR Gurgaon')
