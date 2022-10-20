# I.Przypadek testowy 2
#
# Projekt:
# AutomationPractice
#
# Scenariusz testowy:
# Logowanie użytkownika
#
# Przypadek 002:
# Logowanie do systemu z nieprawidłowymi danymi
#
# Warunki wstępne:
# 1. Otwarta strona główna
#
# Kroki:
# 1. Kliknij link “Sign in”
# 2. Wpisz nieprawidłowy email
# 3. Wpisz nieprawidłowe hasło
# 4. Kliknij przycisk “Sign in”
#
# Oczekiwany rezultat:
# Użytkownikownik dostaje komunikat o błędzie logowania, nie zostaje zalogowany.
#
# Warunki końcowe:
# 1. Logowanie nie powiodło się
#
# II.Automatyzacja przypadku testowego przy pomocy Selenium Webdriver z zastosowaniem Page Object Pattern

# Import niezbędnych bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from faker import Faker

fake = Faker("pl_PL")

# DANE TESTOWE
email_data = fake.email()
password_data = "Olamakoty2!"


class AuthenticationPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(email)
        return self

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, "passwd")
        password_input.send_keys(password)
        return self

    def click_login(self):
        login_button = self.driver.find_element(By.ID, "SubmitLogin")
        login_button.click()
        return self

    def get_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, "alert-danger")
        return error_message.text


class LoginTests(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne testu:

        # Otwarcie przeglądarki
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\magda\OneDrive\Pulpit\geckodriver.exe")

        # Otwarcie strony
        self.driver.get("http://automationpractice.com/")

        # Maksymalizacja okna
        self.driver.maximize_window()

        # Ustawienie bezwarunkowego czekania na element przy wyszukiwaniu maks. 10 sekund
        self.driver.implicitly_wait(10)

    def test_invalid_login(self):
        driver = self.driver

        sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_a.click()

        auth_page = AuthenticationPage(driver) \
            .enter_email(email_data) \
            .enter_password(password_data) \
            .click_login()

        expected_error_message = "There is 1 error"
        self.assertIn(expected_error_message, auth_page.get_error_message())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

# III.Uwagi końcowe
#
# Automatyzacja przypadku testowego powiodła się. Oczekiwany komunikat o błędzie pojawił się na stronie.
# Testowanie może przebiegać wolno, ponieważ strona internetowa jest często używana do nauki testowania oprogramowania.
