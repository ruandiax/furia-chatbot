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
Use um arquivo .env.sample para criar o .env

3. Rode o scrapper para buscar os dados atualizados sobre a Furia!
  docker compose up scrapper --build
3.1 Este container criará um arquivo furia.json no diretório /data

4. Rode frontend para interagir com o chatbot
  docker compose up frontend --build

```
