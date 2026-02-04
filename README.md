# 📧 LangChain Gmail Agent

Agente de IA que envia emails automaticamente via Gmail usando LangChain + Google Gemini.

## 🚀 Funcionalidades

- ✉️ Enviar emails via Gmail usando linguagem natural
- 🤖 Integração com Google Gemini (LLM)
- 🔧 Ferramentas do Gmail: pesquisa, leitura, envio, rascunhos

## 📋 Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes)
- Conta Google com Gmail
- API Key do Google Gemini

## 🔧 Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/ErickGuimaraesFerreira/ai-email-agent-
cd langchain-gmail
```

### 2. Instale as dependências

```bash
uv sync
```

### 3. Configure o Google Cloud Console

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
   - Coloque na raiz do projeto

### 4. Obtenha a API Key do Gemini

1. Acesse [aistudio.google.com](https://aistudio.google.com/)
2. Crie uma API Key
3. Copie a chave

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_API_KEY=sua_api_key_aqui
EMAIL_ADDRESS2=email_destino@gmail.com
```

### 6. Gere o token de autenticação

Na primeira execução, o navegador abrirá para autenticar sua conta Google:

```bash
uv run code.py
```

- Faça login na sua conta
- Autorize o acesso ao Gmail
- O arquivo `token.json` será criado automaticamente

## ▶️ Uso

```bash
uv run code.py
```

O agente enviará um email de teste para o endereço configurado em `EMAIL_ADDRESS2`.

### Personalizando o pedido

Edite a variável `pedido` no `code.py`:

```python
pedido = "Envie um email com o assunto 'Reunião' para fulano@email.com dizendo que a reunião foi confirmada"
```

## 📁 Estrutura do Projeto

```
langchain-gmail/
├── code.py              # Código principal
├── credentials.json     # Credenciais OAuth (não commitar!)
├── token.json           # Token de autenticação (não commitar!)
├── .env                 # Variáveis de ambiente (não commitar!)
├── .gitignore           # Arquivos ignorados pelo git
├── pyproject.toml       # Dependências do projeto
└── README.md
```

## ⚠️ Importante

- **Nunca commite** os arquivos `credentials.json`, `token.json` e `.env`
- Se receber erro `429 RESOURCE_EXHAUSTED`, aguarde alguns segundos ou troque o modelo para `gemini-1.5-flash`
- O app precisa estar em modo de teste no Google Cloud para funcionar sem verificação

## 🛠️ Dependências

- `langchain-google-community[gmail]` - Toolkit do Gmail
- `langchain-google-genai` - Integração com Gemini
- `langgraph` - Framework de agentes
- `python-dotenv` - Carregamento de variáveis de ambiente

## 📝 Licença

MIT
