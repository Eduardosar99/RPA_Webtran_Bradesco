# No seu caso o login já está embutido na URL, então este módulo será mantido como placeholder.
# Pode crescer no futuro se o portal exigir autenticação dinâmica.

def gerar_url_login(login, senha):
    return f"https://{login}:{senha}@os390.bradescoseguros.com.br/suporte/OSdown.html"
