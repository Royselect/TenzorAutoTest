from pages.sbis_main_page import SbisMainPage
from pages.sbis_download_page import SbisDownloadPage

def test_equal_plagin(browser, chrome):
    sbis_main_page = SbisMainPage(browser)
    sbis_main_page.open()
    sbis_main_page.link_download_plagin_click()

    sbis_download_page = SbisDownloadPage(browser, chrome)
    sbis_download_page.download_web_plagin()
    assert sbis_download_page.check_download_web_plagin(), "Не загрузился"