# FURIA Chatbot – Fan Assistant

Um chatbot interativo e **escalável** para fãs do time de CS:GO da FURIA, desenvolvido com **Streamlit**, **Amazon Lex**, **Python** e **Docker**. Ele responde a perguntas sobre o time, escalações, próximos jogos, curiosidades e muito mais — tudo isso em uma estrutura pensada para crescimento e fácil manutenção.

---

## 🔧 Tecnologias utilizadas

- **Python** – Backend e integração com AWS
- **Amazon Lex (V2)** – Processamento de linguagem natural
- **Streamlit** – Interface web simples e rápida
- **Docker** – Conteinerização e portabilidade
- **AWS SDK (boto3)** – Conexão segura com o Lex

---

## 💬 Funcionalidades

- Respostas contextuais sobre o time da FURIA
- Consultas sobre escalações, histórico e próximos jogos
- Experiência via chat com linguagem natural
- Interface acessível diretamente pelo navegador

---

## 🚀 Escalabilidade

Este projeto foi arquitetado para ser facilmente escalado:

- **Modular** – Componentes desacoplados (UI, lógica, integração)
- **Pronto para cloud** – Pode ser implantado em ECS, EC2, Lambda ou GCP/Azure
- **Extensível** – Suporte para novas intents, slots e backends
- **Deploy facilitado** – Basta usar Docker para rodar em qualquer lugar

---

## 🖥️ Interface

> em breve

---

## 📦 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/furia-chatbot.git
cd furia-chatbot

2. Configure as variáveis de ambiente
Crie um arquivo .env na raiz com as seguintes variáveis:

AWS_ACCESS_KEY_ID= Sua chave de acesso
AWS_SECRET_ACCESS_KEY= Sua chave secreta
AWS_DEFAULT_REGION=us-east-1

LEX_BOT_ID=xxxxxxxxxxxx
LEX_BOT_ALIAS_ID=xxxxxxxxxxxx
LEX_LOCALE_ID=pt_BR

Ou use o .env.example como base:
cp .env.example .env

3. Construa a imagem Docker
docker build -t furia-chatbot .

4. Rode o container
docker run --env-file .env -p 8501:8501 furia-chatbot

5. Acesse no navegador
http://localhost:8501
