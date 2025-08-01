import os
from datetime import datetime

from config import PASTA_LOGS

def criar_pastas(*pastas):
    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)

def limpar_pastas(*pastas):
    import shutil
    for pasta in pastas:
        if os.path.exists(pasta):
            shutil.rmtree(pasta)
        os.makedirs(pasta)

def registrar_log(mensagem):
    os.makedirs(PASTA_LOGS, exist_ok=True)
    nome_arquivo = f"log_extracao_{datetime.today().date()}.txt"
    caminho_log = os.path.join(PASTA_LOGS, nome_arquivo)

    with open(caminho_log, "a", encoding="utf-8") as f:
        f.write(f"{mensagem}\n")
    print(mensagem)  # Se quiser ver no console também
