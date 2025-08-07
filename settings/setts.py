from datetime import date
import os


LOGIN_FIXO = "TW06812"
SENHA_FIXA = "yy123yc"
COD_1 = "SSCFR58U"
COD_2 = "SSCFR59U"


DATA_HOJE = str(date.today())

# Caminho absoluto da pasta onde o script está sendo executado
BASE_DIR = os.getcwd()

PASTA_BASE = os.path.join(BASE_DIR, "Arquivos_Webtran")

# Pasta onde os arquivos baixados serão armazenados, nomeada com login e data
PASTA_DOWNLOAD = os.path.join(PASTA_BASE, f"{LOGIN_FIXO}_{DATA_HOJE}")

# Pasta para os arquivos processados e filtrados
PASTA_GERAL_FILTRADA = os.path.join(PASTA_BASE, f"Webtran_Bradesco_{DATA_HOJE}")

# Pasta para uma versão da rotina com outro formato ou regras
PASTA_ROTINA = os.path.join(PASTA_BASE, f"Webtran_Bradesco_Rotina_{DATA_HOJE}")


PASTA_DESTINO_GERAL = r"C:\Users\Eduar\Documents\Webtram_Bradesco_Geral"
PASTA_DESTINO_ROTINA = r"C:\Users\Eduar\Documents\SherPoint_Bradesco_Rotina"

# Pasta onde os arquivos de log serão salvos
PASTA_LOGS = os.path.join(BASE_DIR, "Logs_Webtran")
