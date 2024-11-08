from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class SbisDownloadPage(BasePage):
    URL = 'https://sbis.ru/download/'
    link_download_web_plagin = (By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')


    def __init__(self, browser, chrome):
        super().__init__(browser, chrome)
        self.download_dir = chrome.download

    def open(self):
        self.browser.get(self.URL)

    def link_download_web_plagin_get(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.link_download_web_plagin)
        )
        return self.find(self.link_download_web_plagin)

    def download_web_plagin(self):
        element = self.link_download_web_plagin_get()
        self.chrome.driver.get(element.get_attribute('href'))
        self.wait_for_download_complete()
        
    def wait_for_download_complete(self):
        filename = "sbisplugin-setup-web.exe"  # Ожидаем конкретный файл
        file_path = self.download_dir / filename
        
        # Ждем, пока файл начнет загружаться
        while not file_path.exists():
            time.sleep(1)

        # Ждем, пока файл завершит загрузку
        while True:
            if file_path.exists():
                # Проверяем размер файла
                original_size = os.path.getsize(file_path)
                time.sleep(1)  # Ждем секунду, прежде чем проверять снова
                if os.path.getsize(file_path) == original_size:
                    break  # Если размер файла не изменился, выходим

        print(f"Файл {filename} успешно загружен.")

    def check_download_web_plagin(self):
        return (self.chrome.download / "sbisplugin-setup-web.exe").exists()