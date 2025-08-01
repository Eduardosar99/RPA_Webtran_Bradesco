import os
import shutil
import zipfile
from collections import defaultdict
from config import *
from utils import registrar_log

def organizar_e_enviar():
    pasta_login = os.path.join(PASTA_GERAL_FILTRADA, f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(pasta_login, exist_ok=True)

    for arquivo in os.listdir(PASTA_DOWNLOAD):
        if arquivo.endswith(".zip"):
            zip_path = os.path.join(PASTA_DOWNLOAD, arquivo)
            destino = os.path.join(pasta_login, arquivo)
            shutil.copy2(zip_path, destino)
            with zipfile.ZipFile(destino, 'r') as zip_ref:
                zip_ref.extractall(pasta_login)

    for nome in os.listdir(pasta_login):
        if nome.endswith(".zip"):
            os.remove(os.path.join(pasta_login, nome))

    destino_final = os.path.join(PASTA_DESTINO_GERAL, f"Webtram_Bradesco_{DATA_HOJE}", f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(destino_final, exist_ok=True)

    for nome in os.listdir(pasta_login):
        origem = os.path.join(pasta_login, nome)
        destino = os.path.join(destino_final, nome)
        if not os.path.exists(destino):
            shutil.copy2(origem, destino)

    registrar_log(f"🗂️ Arquivos organizados na pasta local: {LOGIN_FIXO}")
    registrar_log("📂 Arquivos Enviados para o SharePoint Geral")


def organizar_por_codigo_e_enviar():
    pasta_rotina_login = os.path.join(PASTA_ROTINA, f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(pasta_rotina_login, exist_ok=True)

    for arquivo in os.listdir(PASTA_DOWNLOAD):
        if arquivo.endswith(".zip"):
            zip_path = os.path.join(PASTA_DOWNLOAD, arquivo)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(pasta_rotina_login)

    arquivos_validos = [f for f in os.listdir(pasta_rotina_login) if f[:2] in ["PC", "SN", "PS"] and f[2:8].isdigit()]
    grupos = defaultdict(list)

    for nome in arquivos_validos:
        codigo = nome[2:8]
        grupos[codigo].append(nome)

    for codigo, arquivos in grupos.items():
        pasta_codigo = os.path.join(pasta_rotina_login, codigo)
        os.makedirs(pasta_codigo, exist_ok=True)
        for nome in arquivos:
            shutil.move(os.path.join(pasta_rotina_login, nome), os.path.join(pasta_codigo, nome))

    destino_rotina = os.path.join(PASTA_DESTINO_ROTINA, f"Bradesco_Rotina_{DATA_HOJE}", f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(destino_rotina, exist_ok=True)

    for codigo in grupos:
        origem = os.path.join(pasta_rotina_login, codigo)
        destino = os.path.join(destino_rotina, codigo)
        if not os.path.exists(destino):
            shutil.copytree(origem, destino)

    registrar_log("📂 Arquivos Enviados para o SharePoint Rotina")
