import time
from settings.setts import PASTA_DOWNLOAD, PASTA_GERAL_FILTRADA, PASTA_ROTINA
from core.helpers import limpar_pastas, criar_pastas, registrar_log
from core.extract import realizar_extracao
from core.process import organizar_e_enviar, organizar_por_codigo_e_enviar
from datetime import datetime

inicio = time.time()

# Limpa as pastas utilizadas e recria o ambiente do RPA do zero
limpar_pastas(PASTA_DOWNLOAD, PASTA_GERAL_FILTRADA, PASTA_ROTINA)

# Registra no log que a limpeza foi concluída com sucesso
registrar_log("🧼 Ambiente limpo e pastas recriadas.")

# Inicia o bloco principal com tratamento de erro
try:
    # Executa o processo de extração (acessa o site e baixa os arquivos)
    realizar_extracao()
    organizar_e_enviar()
    organizar_por_codigo_e_enviar()

    fim = time.time()
    
    registrar_log(f"📌 Processo finalizado com sucesso em: {datetime.now().strftime('%d/%m/%Y')}")

    # Calcula o tempo total de execução (em horas, minutos e segundos)
    duracao = fim - inicio
    horas, resto = divmod(duracao, 3600)
    minutos, segundos = divmod(resto, 60)

    # Registra no log o tempo total de execução de forma formatada
    registrar_log(f"⏱️ Tempo total de execução: {int(horas):02}h {int(minutos):02}min {int(segundos):02}s")

# Se algum erro ocorrer em qualquer etapa, ele será capturado aqui
except Exception as e:
    # Registra o erro no log
    registrar_log(f"❌ Erro inesperado: {str(e)}")
    raise
