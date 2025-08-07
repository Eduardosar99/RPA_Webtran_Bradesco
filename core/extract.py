from playwright.sync_api import sync_playwright
import os
from settings.setts import LOGIN_FIXO, SENHA_FIXA, COD_1, COD_2, PASTA_DOWNLOAD

# Importa a função que gera a URL com autenticação embutida
from core.auth import gerar_url_login

from core.helpers import registrar_log

# Função principal de extração
def realizar_extracao():
    # Registra início da extração no log
    registrar_log(f"🔁 Extração iniciada para o login : {LOGIN_FIXO}")

    with sync_playwright() as p:
        # Inicia navegador Chromium em modo visível (headless=False)
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(accept_downloads=True)

        # Abre uma nova página (aba)
        page = context.new_page()

        # Acessa a URL de login com autenticação embutida
        page.goto(gerar_url_login(LOGIN_FIXO, SENHA_FIXA))

        # Loop para processar os dois códigos (COD_1 e COD_2)
        for codigo in [COD_1, COD_2]:
            campo = page.locator('input[name="CODTRAN"]')

            # Dá foco no campo
            campo.click()
            page.dispatch_event('input[name="CODTRAN"]', 'focus')

            # Limpa qualquer conteúdo anterior com Ctrl+A e Delete
            page.keyboard.press('Control+A')
            page.keyboard.press('Delete')

            # Digita o novo código
            page.keyboard.type(codigo)

            # Dispara o evento de "blur" (perda de foco), como se saísse do campo
            page.dispatch_event('input[name="CODTRAN"]', 'blur')

            # Aguarda o início do download após o clique no botão de submit
            with page.expect_download() as download_info:
                page.click('input[type="submit"]')  # Clica no botão de envio

            # Quando o download estiver disponível, salva o arquivo na pasta configurada
            download = download_info.value
            download.save_as(os.path.join(PASTA_DOWNLOAD, download.suggested_filename))

        # Fecha o navegador ao final da rotina
        browser.close()

    # Log de conclusão
    registrar_log(f"⬇️ Arquivos baixados para: {LOGIN_FIXO}")
    registrar_log(f"✅ Extração concluída para o login: {LOGIN_FIXO}")
