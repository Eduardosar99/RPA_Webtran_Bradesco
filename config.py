from datetime import date
import os

# Configurações fixas
LOGIN_FIXO = "TW06812"
SENHA_FIXA = "yy123yb"
COD_1 = "SSCFR58U"
COD_2 = "SSCFR59U"

# Datas e diretórios
DATA_HOJE = str(date.today())

BASE_DIR = os.getcwd()
PASTA_BASE = os.path.join(BASE_DIR, "Arquivos_Webtran")

PASTA_DOWNLOAD = os.path.join(PASTA_BASE, f"{LOGIN_FIXO}_{DATA_HOJE}")
PASTA_GERAL_FILTRADA = os.path.join(PASTA_BASE, f"Webtran_Bradesco_{DATA_HOJE}")
PASTA_ROTINA = os.path.join(PASTA_BASE, f"Webtran_Bradesco_Rotina_{DATA_HOJE}")

PASTA_DESTINO_GERAL = r"C:\Users\Eduar\Documents\Webtram_Bradesco_Geral"
PASTA_DESTINO_ROTINA = r"C:\Users\Eduar\Documents\SherPoint_Bradesco_Rotina"

PASTA_LOGS = os.path.join(BASE_DIR, "Logs_Webtran")
