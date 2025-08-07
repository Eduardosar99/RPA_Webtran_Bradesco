import os
from datetime import datetime

from settings.setts import PASTA_LOGS

def criar_pastas(*pastas):
    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)

# Função para limpar (deletar e recriar) pastas
def limpar_pastas(*pastas):
    import shutil 

    for pasta in pastas:
        if os.path.exists(pasta):
            shutil.rmtree(pasta)
        os.makedirs(pasta)

# Função para registrar logs em arquivo e console
def registrar_log(mensagem):
    os.makedirs(PASTA_LOGS, exist_ok=True)

    # Cria o nome do arquivo de log com base na data do dia
    nome_arquivo = f"log_extracao_{datetime.today().date()}.txt"

    # Caminho completo do arquivo de log
    caminho_log = os.path.join(PASTA_LOGS, nome_arquivo)

    # Abre o arquivo no modo append ("a") e escreve a nova mensagem
    with open(caminho_log, "a", encoding="utf-8") as f:
        f.write(f"{mensagem}\n")
    print(mensagem)
