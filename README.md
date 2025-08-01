
# 🤖 RPA Webtran Bradesco

Este projeto é um **RPA (Robotic Process Automation)** desenvolvido com **Python + Playwright** para automatizar o processo de **login, extração, organização e envio de arquivos** do sistema **Webtran Bradesco**.


---

## 🚀 Funcionalidades

- Login automático via autenticação embutida na URL
- Extração de arquivos `.zip` 
- Organização e agrupamento de arquivos por código
- Envio dos arquivos organizados para diretórios finais (Geral e Rotina)
- Registro de logs com timestamp
- Estrutura modular e escalável

---

## 🧱 Estrutura do Projeto

```text
AUTOBOTS/
│
├── Arquivos_Webtran/              # Pasta onde são salvos os arquivos extraídos e processados (gerada automaticamente)
├── Logs_Webtran/                  # Pasta onde ficam os arquivos de log gerados durante a execução
│
├── auth.py                        # Gera a URL de login automática para o sistema Webtran
├── config.py                      # Contém todas as configurações fixas, credenciais e caminhos utilizados
├── extracao.py                    # Módulo responsável pela automação Playwright que realiza a extração dos arquivos
├── gcp_query.py                   # (Futuro) Integração com GCP para envio ou consulta de dados
├── main.py                        # Script principal que orquestra toda a rotina (limpa, extrai, organiza, envia)
├── processamento.py               # Organiza os arquivos extraídos e realiza o envio para os diretórios finais
├── utils.py                       # Funções auxiliares para logs, criação e limpeza de pastas
│
├── requirements.txt               # Lista de dependências do projeto (Playwright, etc.)
└── venv/                         
```


---

## ▶️ Como Executar

```bash
python main.py
```

A execução realiza os seguintes passos:

1. Limpa e recria as pastas da rotina.
2. Acessa o sistema Webtran via navegador automatizado.
3. Baixa os arquivos dos dois códigos definidos.
4. Organiza os arquivos e envia para os diretórios locais (Geral e Rotina).
5. Registra logs com duração e status da operação.

---

## 📁 Pastas Geradas

- `Arquivos_Webtran/` — onde ficam os arquivos baixados, organizados e prontos para envio.
- `Logs_Webtran/` — onde são salvos os arquivos `.txt` com os registros de execução, incluindo data, tempo e possíveis erros.

---

## ✅ Status do Projeto

- [x] Módulos principais implementados e testados
- [x] RPA funcional com login e download
- [x] Organização por código e envio para pastas locais
- [ ] Integração com GCP (em andamento)

---

