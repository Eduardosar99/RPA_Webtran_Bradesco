import os
import shutil
import zipfile
from collections import defaultdict

from settings.setts import *

from core.helpers import registrar_log

# ORGANIZAÇÃO GERAL E ENVIO PARA A PASTA DE DESTINO GERAL
def organizar_e_enviar():
    # Cria pasta temporária com base no login e na data
    pasta_login = os.path.join(PASTA_GERAL_FILTRADA, f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(pasta_login, exist_ok=True)

    # Copia e extrai todos os arquivos .zip da pasta de download
    for arquivo in os.listdir(PASTA_DOWNLOAD):
        if arquivo.endswith(".zip"):
            zip_path = os.path.join(PASTA_DOWNLOAD, arquivo)
            destino = os.path.join(pasta_login, arquivo)
            shutil.copy2(zip_path, destino)

            # Extrai o conteúdo do .zip para a pasta de login
            with zipfile.ZipFile(destino, 'r') as zip_ref:
                zip_ref.extractall(pasta_login)

    # Remove os arquivos .zip após a extração
    for nome in os.listdir(pasta_login):
        if nome.endswith(".zip"):
            os.remove(os.path.join(pasta_login, nome))

    # Define o caminho final onde os arquivos serão copiados
    destino_final = os.path.join(PASTA_DESTINO_GERAL, f"Webtram_Bradesco_{DATA_HOJE}", f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(destino_final, exist_ok=True)

    # Copia todos os arquivos processados para o destino final
    for nome in os.listdir(pasta_login):
        origem = os.path.join(pasta_login, nome)
        destino = os.path.join(destino_final, nome)
        if not os.path.exists(destino):
            shutil.copy2(origem, destino)

    # Registra sucesso da organização e envio
    registrar_log(f"🗂️ Arquivos organizados na pasta local: {LOGIN_FIXO}")
    registrar_log("📂 Arquivos Enviados para o SharePoint Geral")


# ORGANIZAÇÃO POR CÓDIGO E ENVIO PARA DESTINO ROTINA
def organizar_por_codigo_e_enviar():
    # Cria a pasta de rotina com nome baseado no login
    pasta_rotina_login = os.path.join(PASTA_ROTINA, f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(pasta_rotina_login, exist_ok=True)

    # Extrai os .zip diretamente para a pasta de rotina
    for arquivo in os.listdir(PASTA_DOWNLOAD):
        if arquivo.endswith(".zip"):
            zip_path = os.path.join(PASTA_DOWNLOAD, arquivo)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(pasta_rotina_login)

    # Filtra arquivos cujo nome começa com PC, SN ou PS, seguido de 6 dígitos
    arquivos_validos = [f for f in os.listdir(pasta_rotina_login) if f[:2] in ["PC", "SN", "PS"] and f[2:8].isdigit()]

    # Agrupa os arquivos pelo código de 6 dígitos (posição 3 a 8)
    grupos = defaultdict(list)

    for nome in arquivos_validos:
        codigo = nome[2:8]
        grupos[codigo].append(nome)

    # Cria subpastas para cada código e move os arquivos correspondentes
    for codigo, arquivos in grupos.items():
        pasta_codigo = os.path.join(pasta_rotina_login, codigo)
        os.makedirs(pasta_codigo, exist_ok=True)
        for nome in arquivos:
            shutil.move(os.path.join(pasta_rotina_login, nome), os.path.join(pasta_codigo, nome))

    # Define o caminho final de destino da rotina
    destino_rotina = os.path.join(PASTA_DESTINO_ROTINA, f"Bradesco_Rotina_{DATA_HOJE}", f"{LOGIN_FIXO}_{DATA_HOJE}")
    os.makedirs(destino_rotina, exist_ok=True)

    # Copia as subpastas por código para o destino final
    for codigo in grupos:
        origem = os.path.join(pasta_rotina_login, codigo)
        destino = os.path.join(destino_rotina, codigo)
        if not os.path.exists(destino):
            shutil.copytree(origem, destino)

    # Registra sucesso do envio para rotina
    registrar_log("📂 Arquivos Enviados para o SharePoint Rotina")
