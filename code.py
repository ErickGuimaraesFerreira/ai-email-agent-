import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_google_credentials,
)
from langgraph.prebuilt import create_react_agent

# Carregar variáveis de ambiente
load_dotenv()

# declara a variável de credenciais do gmail
credentials = get_google_credentials(
    scopes=["https://mail.google.com/"],
    token_file="token.json",
    client_secrets_file="credentials.json",
)

# Construir o serviço do Gmail
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)
tools = toolkit.get_tools()

# Configurar o modelo LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.environ.get("GOOGLE_API_KEY"),
)

# Criar o agente com as ferramentas do Gmail
agente = create_react_agent(llm, tools)

# mensagem para o agente
pedido = f"Envie um email dizendo 'Olá' para o email {os.environ.get("EMAIL_ADDRESS1")}"
# executar o agente
for step in agente.stream({"messages": [("user", pedido)]}):
    if "messages" in step:
        for message in step["messages"]:
            message.pretty_print()

print(f"Email enviado com sucesso para {os.environ.get("EMAIL_ADDRESS1")}")
