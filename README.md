# 🤖 RPA Webtran Bradesco

Este projeto é um **RPA (Robotic Process Automation)** desenvolvido com **Python + Playwright** para automatizar o processo de **login, extração, organização e envio de arquivos** do sistema **Webtran Bradesco**.  
O projeto foi estruturado com foco em **organização modular**, **boas práticas** e **fácil manutenção**, além de estar preparado para futura integração com **Google Cloud Platform (BigQuery)**.

---

## 📌 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Playwright](https://playwright.dev/python/)
- [Pandas](https://pandas.pydata.org/)
- [Logging](https://docs.python.org/3/library/logging.html) para monitoramento e depuração

---

## 🚀 Funcionalidades

- Login automático via autenticação embutida na URL
- Extração de arquivos `.zip` de dois códigos distintos
- Organização e agrupamento de arquivos por código
- Envio dos arquivos organizados para diretórios finais (Geral e Rotina)
- Registro de logs com timestamp
- Estrutura modular e escalável

---

## 📂 Estrutura do Projeto

```bash
RPA_Webtran_Bradesco/
│
├── Arquivos_Webtran/      # Arquivos extraídos e organizados pela rotina (gerado automaticamente)
├── Logs_Webtran/          # Arquivos de log com registro de execução
│
├── core/                          # Módulos principais da automação
│   ├── auth.py                    # Geração da URL de login automática para o sistema Webtran
│   ├── extract.py                 # Automação com Playwright para extração dos arquivos
│   ├── helpers.py                 # Funções auxiliares (logs, manipulação de arquivos, diretórios.
│   └── process.py                 # Processamento e organização dos arquivos extraídos
│
├── services/                      # Camada de integração externa
│   ├── Access_gcp/                # Conexão e autenticação com serviços do GCP
│   └── database.py                # Módulo para armazenar as querys do GCP
│
├── settings/                      # Configurações globais do projeto
│   └── setts.py                   # Caminhos e parâmetros usados na rotina
│
├── main.py                # Script principal que orquestra toda a rotina
├── requirements.txt       # Dependências do projeto
└── .gitignore             # Arquivos/pastas ignorados pelo Git
```

---

## 🧩 Módulos Explicados

- **`core/`** → Contém a lógica central da automação, incluindo abertura do navegador, login, navegação e extração de dados.
- **`services/`** → Responsável por integrações externas, como BigQuery e APIs.
- **`settings/`** → Armazena configurações e parâmetros do projeto.
- **`Arquivos_Webtran/`** → Local de armazenamento dos arquivos baixados automaticamente.
- **`Logs_Webtran/`** → Contém logs detalhados de cada execução, útil para auditoria e debug.

---

## ▶️ Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/RPA_Webtran_Bradesco.git
cd RPA_Webtran_Bradesco
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as credenciais**
- As credenciais do Google Cloud devem ser colocadas **localmente** na pasta `services/Access_gcp/` (essa pasta não é versionada).

5. **Execute o projeto**
```bash
python main.py
```

---

## 📋 Status do Projeto

✅ Estrutura modular  
✅ Extração de dados via Playwright  
✅ Salvamento local de arquivos e logs  
⚙ Integração com Google BigQuery *(em andamento)*

---

## 👨‍💻 Autor

Desenvolvido por **Eduardo**  

---
