import time
from config import PASTA_DOWNLOAD, PASTA_GERAL_FILTRADA, PASTA_ROTINA
from utils import limpar_pastas, criar_pastas, registrar_log
from extracao import realizar_extracao
from processamento import organizar_e_enviar, organizar_por_codigo_e_enviar
from datetime import datetime

inicio = time.time()
limpar_pastas(PASTA_DOWNLOAD, PASTA_GERAL_FILTRADA, PASTA_ROTINA)
registrar_log("🧼 Ambiente limpo e pastas recriadas.")

try:
    realizar_extracao()
    organizar_e_enviar()
    organizar_por_codigo_e_enviar()
    fim = time.time()

    registrar_log(f"📌 Processo finalizado com sucesso em: {datetime.now().strftime('%d/%m/%Y')}")
    duracao = fim - inicio
    horas, resto = divmod(duracao, 3600)
    minutos, segundos = divmod(resto, 60)
    registrar_log(f"⏱️ Tempo total de execução: {int(horas):02}h {int(minutos):02}min {int(segundos):02}s")

except Exception as e:
    registrar_log(f"❌ Erro inesperado: {str(e)}")
    raise
