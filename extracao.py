from playwright.sync_api import sync_playwright
import os
from config import LOGIN_FIXO, SENHA_FIXA, COD_1, COD_2, PASTA_DOWNLOAD
from auth import gerar_url_login
from utils import registrar_log

def realizar_extracao():
    registrar_log(f"🔁 Extração iniciada para o login : {LOGIN_FIXO}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        page.goto(gerar_url_login(LOGIN_FIXO, SENHA_FIXA))

        for codigo in [COD_1, COD_2]:
            campo = page.locator('input[name="CODTRAN"]')
            campo.click()
            page.dispatch_event('input[name="CODTRAN"]', 'focus')
            page.keyboard.press('Control+A')
            page.keyboard.press('Delete')
            page.keyboard.type(codigo)
            page.dispatch_event('input[name="CODTRAN"]', 'blur')

            with page.expect_download() as download_info:
                page.click('input[type="submit"]')
            download = download_info.value
            download.save_as(os.path.join(PASTA_DOWNLOAD, download.suggested_filename))

        browser.close()

    registrar_log(f"⬇️ Arquivos baixados para: {LOGIN_FIXO}")
    registrar_log(f"✅ Extração concluída para o login: {LOGIN_FIXO}")
