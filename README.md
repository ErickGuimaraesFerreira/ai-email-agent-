<div align="center">

# 📧 AI Email Agent

### Automatize seus emails com Inteligência Artificial

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Gmail API](https://img.shields.io/badge/Gmail-API-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](https://developers.google.com/gmail/api)

---

**Envie emails usando linguagem natural • Google Gemini**

</div>

---

## 🎯 O que é este projeto?

Um **agente de IA** que permite enviar emails automaticamente via Gmail usando apenas **comandos em linguagem natural**.

> 💬 *"Envie um email para fulano@email.com dizendo que a reunião foi confirmada"*

O agente interpreta seu pedido e executa a ação automaticamente!

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| ✉️ **Enviar emails** | Compose e envie emails usando linguagem natural |
| 🔍 **Pesquisar emails** | Busque emails na sua caixa de entrada |
| 📖 **Ler emails** | Acesse o conteúdo de emails específicos |
| � **Criar rascunhos** | Salve emails como rascunho para revisão |
| 🤖 **IA Generativa** | Powered by Google Gemini |

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                     USUÁRIO                             │
│              "Envie um email para..."                   │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  LANGCHAIN AGENT                        │
│    ┌─────────────┐    ┌─────────────┐                   │
│    │   Gemini    │◄──►│   ReAct     │                   │
│    │    LLM      │    │   Agent     │                   │
│    └─────────────┘    └──────┬──────┘                   │
└──────────────────────────────┼──────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────┐
│                  GMAIL TOOLKIT                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│  │  Search  │ │   Read   │ │   Send   │ │  Draft   │    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘    │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                    GMAIL API                            │
└─────────────────────────────────────────────────────────┘
```

---

## � Quick Start

### Pré-requisitos

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** - Gerenciador de pacotes
- **Conta Google** com Gmail
- **API Key** do Google Gemini

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/ErickGuimaraesFerreira/ai-email-agent-
cd langchain-gmail
```

### 2️⃣ Instale as dependências

```bash
uv sync
```

### 3️⃣ Configure o Google Cloud

<details>
<summary>📋 Clique para ver o passo a passo</summary>

1. Acesse [console.cloud.google.com](https://console.cloud.google.com/)
2. Crie um novo projeto
3. Habilite a **Gmail API**:
   - Menu → APIs & Services → Library
   - Pesquise "Gmail API" → Enable

4. Configure a tela de consentimento OAuth:
   - APIs & Services → OAuth consent screen
   - Selecione "External"
   - Preencha nome do app e email
   - Em Scopes, adicione: `https://mail.google.com/`
   - Em Test users, adicione seu email

5. Crie as credenciais OAuth:
   - APIs & Services → Credentials
   - Create Credentials → OAuth client ID
   - Selecione **Desktop app**
   - Baixe o JSON e renomeie para `credentials.json`

</details>

### 4️⃣ Configure as variáveis

Crie um arquivo `.env`:

```env
GOOGLE_API_KEY=sua_api_key_aqui
EMAIL_ADDRESS1=email_destino@gmail.com
```

### 5️⃣ Execute

```bash
uv run code.py
```

> 🔐 Na primeira execução, autentique sua conta Google no navegador.

---

## 💻 Exemplo de Uso

```python
# Defina seu pedido em linguagem natural
pedido = "Envie um email com o assunto 'Reunião' para fulano@email.com 
          dizendo que a reunião foi confirmada para amanhã às 14h"

# O agente processa e executa automaticamente
for step in agente.stream({"messages": [("user", pedido)]}):
    if "messages" in step:
        for message in step["messages"]:
            message.pretty_print()
```

---

## 📁 Estrutura do Projeto

```
langchain-gmail/
├── 📄 code.py              # Código principal do agente
├── 🔐 credentials.json     # Credenciais OAuth (ignorado pelo git)
├── 🔐 token.json           # Token de autenticação (ignorado pelo git)
├── 🔐 .env                 # Variáveis de ambiente (ignorado pelo git)
├── 📋 .gitignore           # Arquivos ignorados pelo git
├── 📦 pyproject.toml       # Dependências do projeto
└── 📖 README.md
```

---

## 🛠️ Stack Tecnológica

<div align="center">

| Tecnologia | Função |
|------------|--------|
| **LangChain** | Framework de agentes |
| **LangGraph** | Orquestração de agentes |
| **Google Gemini** | Modelo de linguagem (LLM) |
| **Gmail API** | Integração com Gmail |
| **Python-dotenv** | Gerenciamento de variáveis |

</div>

---

## ⚠️ Observações

> [!IMPORTANT]
> O app precisa estar em **modo de teste** no Google Cloud para funcionar sem verificação.

> [!WARNING]
> Nunca compartilhe seus arquivos `credentials.json`, `token.json` e `.env`!

---

## 📝 Licença

Este projeto está sob a licença **MIT**.

---

<div align="center">

**Feito com ❤️ usando LangChain + Google Gemini**

[⬆ Voltar ao topo](#-ai-email-agent)

</div>
