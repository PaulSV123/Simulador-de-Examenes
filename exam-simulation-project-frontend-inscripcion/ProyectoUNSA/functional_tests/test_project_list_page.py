from selenium import webdriver
from simulador.models import Postulante
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
    def tearDown(self):
        self.browser.close()
    def login(self):
        self.browser.get('http://localhost:8002/')
        time.sleep(5)
        log = self.browser.find_element_by_name("Login")
        log.click()
        time.sleep(5)
        usuario = self.browser.find_element_by_name("username")
        usuario.send_keys("JesusT")
        time.sleep(5)
        contraseña = self.browser.find_element_by_name("password")
        contraseña.send_keys("ursa-sillballer")
        time.sleep(5)
        env = self.browser.find_element_by_name("Enviar")
        env.click()
        time.sleep(5)