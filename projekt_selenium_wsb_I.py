# I.	Przypadek testowy
#
# Projekt:
# AutomationPractice
#
# Scenariusz testowy:
# Rejestracja nowego użytkownika
#
# Przypadek 001:
# Rejestracja do systemu z prawidłowymi danymi
#
# Warunki wstępne:
# 1.	Otwarta strona główna
# Kroki:
# 1.	Kliknij „Sign in”
# 2.	Wpisz e-mail
# 3.	Kliknij przycisk „Create account”
# 4.	Wybierz płeć
# 5.	Wpisz imię
# 6.	Wpisz nazwisko
# 7.	Sprawdź czy e-mail w polu Email jest taki sam jak wpisany wcześniej
# 8.	Wpisz hasło
# 9.	Wybierz datę urodzenia
# 10.	 Sprawdź czy w polu „First name” jest imię wpisane wcześniej
# 11.	 Sprawdź czy w polu „Last name” jest nazwisko wpisane wcześniej
# 12.	 Wpisz adres
# 13.	 Wpisz miasto
# 14.	 Wybierz stan
# 15.	 Wpisz kod pocztowy
# 16.	 Wpisz nr telefonu komórkowego
# 17.	 Wpisz alias adresu
# 18.	 Kliknij Register
# 19.	 Sprawdź czy na stronie pojawiło się imię i nazwisko zalogowanego użytkownika
#
# Oczekiwany rezultat:
# 	Użytkownikowi udaje się zarejestrować do systemu
#
# Warunki końcowe:
# 1.	Konto zostaje założone

# II.Automatyzacja przypadku testowego przy pomocy Selenium Webdriver

# Import niezbędnych bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.select import Select
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker("pl_PL")

# DANE TESTOWE
email = fake.email()
sex = "F"  # or "M"
first_name = "Magdalena"
last_name = fake.last_name()
password = "Olamakoty2!"
birth_day = "25"
birth_month = "02"
birth_year = "1990"
address = "Kozielska 56"
city = "Miechów"
state = "Alabama"
postal_code = "79531"
phone = fake.phone_number()
alias = "Misiu"


class AutomationpracticeRegistration(unittest.TestCase):

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

    def test_Successful_Registration(self):
        driver = self.driver

        # KROKI:

        # 1. Kliknij "Sign in"
        sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        sign_in_a.click()

        # 2. Wpisz e-mail
        email_input = self.wait_until(20, By.ID, "email_create")
        email_input.send_keys(email)

        # 3. Kliknij przycisk "Create account"
        create_account_btn = driver.find_element(By.ID, "SubmitCreate")
        create_account_btn.click()

        # 4. Wybierz płeć
        if sex == "F":

            # Wybierz Mrs
            driver.find_element(By.ID, "id_gender2").click()
        else:
            # Wybierz Mr
            driver.find_element(By.ID, "id_gender1").click()

        # 5. Wpisz imię
        firstname_input = driver.find_element(By.ID, "customer_firstname")
        firstname_input.send_keys(first_name)

        # 6. Wpisz nazwisko
        last_name_input = driver.find_element(By.ID, "customer_lastname")
        last_name_input.send_keys(last_name)

        # 7. Sprawdź czy e-mail w polu Email jest taki sam jak wpisany wcześniej
        email_check = driver.find_element(By.ID, "email")
        email_expected = email

        # Pobierz e-mail, który wcześniej wpisałaś w polu
        email_fact = email_check.get_attribute("value")

        # Porównaj oba e-maile, ten faktyczny z oczekiwanym
        self.assertEqual(email_expected, email_fact)

        # 8. Wpisz hasło
        password_input = driver.find_element(By.ID, "passwd")
        password_input.send_keys(password)

        # 9. Wybierz datę urodzenia
        days_s = Select(driver.find_element(By.ID, "days"))
        days_s.select_by_value(birth_day)
        months_s = Select(driver.find_element(By.ID, "months"))
        months_s.select_by_value(str(int(birth_month)))
        years_s = Select(driver.find_element(By.ID, "years"))
        years_s.select_by_value(birth_year)

        # 10. Sprawdź czy w polu "First name" jest imię wpisane wcześniej
        address_name_input = driver.find_element(By.ID, "firstname")
        address_name_fact = address_name_input.get_attribute("value")
        first_name_expected = first_name
        self.assertEqual(first_name_expected, address_name_fact)

        # 11. Sprawdź czy w polu "Last name" jest nazwisko wpisane wcześniej
        address_lastname_input = driver.find_element(By.ID, "lastname")
        address_lastname_fact = address_lastname_input.get_attribute("value")
        last_name_expected = last_name
        self.assertEqual(last_name_expected, address_lastname_fact)

        # 12. Wpisz adres
        addres_input = driver.find_element(By.ID, "address1")
        addres_input.send_keys(address)

        # 13. Wpisz miasto
        city_input = driver.find_element(By.ID, "city")
        city_input.send_keys(city)

        # 14. Wybierz stan
        state_select = Select(driver.find_element(By.ID, "id_state"))
        state_select.select_by_visible_text(state)

        # 15. Wpisz kod pocztowy
        postal_code_input = driver.find_element(By.ID, "postcode")
        postal_code_input.send_keys(postal_code)

        # 16. Wpisz numer telefonu komórkowego
        phone_input = driver.find_element(By.ID, "phone_mobile")
        phone_input.send_keys(phone)

        # 17. Wpisz alias adresu
        address_alias = driver.find_element(By.ID, "alias")
        address_alias.clear()
        address_alias.send_keys(alias)

        # 18. Kliknij Register
        register_btn = driver.find_element(By.ID, "submitAccount")
        register_btn.click()

        # 19. Sprawdź czy na stronie pojawiło się imię i nazwisko zalogowanego użytkownika
        username_link = self.wait_until(20, By.CLASS_NAME, "account")
        username_fact = username_link.text
        username_expected = first_name + " " + last_name
        self.assertEqual(username_expected, username_fact)

    def tearDown(self):
        self.driver.quit()
        pass

    def wait_until(self, timeout, locator, text): #https://selenium-python.readthedocs.io/waits.html
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator, text)))
        return element


if __name__ == '__main__':
    unittest.main(verbosity=2)

# III.Uwagi końcowe

# Automatyzacja przypadku testowego powiodła się. Rejestracja nowego użytkownika przebiegła pomyślnie.
# Testowanie może przebiegać wolno, ponieważ strona internetowa jest często używana do nauki testowania oprogramowania.


