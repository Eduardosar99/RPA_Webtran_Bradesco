# Define uma função que gera uma URL com login e senha embutidos
def gerar_url_login(login, senha):
    # Retorna a URL formatada com autenticação básica HTTP embutida
    return f"https://{login}:{senha}@os390.bradescoseguros.com.br/suporte/OSdown.html"
