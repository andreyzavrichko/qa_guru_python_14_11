from pathlib import Path

from selene import browser, have


class RegistrationForm:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form/')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def type_birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element('[value="4"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="2014"]').click()
        browser.element('.react-datepicker__day--015').click()

    def click_gender(self):
        browser.element('[value=Male]+label').click()

    def type_phone(self, phone):
        browser.element('#userNumber').type(phone)

    def type_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def click_hobbies(self):
        browser.element('[for=hobbies-checkbox-1]').click()

    def upload_photo(self, photo):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def press_submit(self):
        browser.element('#submit').click()

    def should_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(have.text(text))

    def should_exact_text(self, first_name, email, gender, phone, birthday, hobbies, hobbies2, photo, address, city):
        browser.element('.table').all('td').even.should(have.exact_texts(first_name, email, gender, phone,
                                                                         birthday, hobbies, hobbies2, photo, address,
                                                                         city))
