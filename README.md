# GuIIOTTI - Website Institucional

![GuIIOTTI Logo](static/img/logo.jpg)

Website institucional e portfólio para a **GuIIOTTI - Soluções em IIoT & Automação**, desenvolvido com Flask. O site apresenta os serviços da empresa, informações de contato e funcionalidades dinâmicas.

**[➡️ Acesse a versão ao vivo aqui](https://guiiotti.onrender.com/)**

---

## ✨ Principais Funcionalidades

-   **Multi-idioma:** Suporte completo para Português (🇧🇷), Inglês (🇬🇧) e Espanhol (🇪🇸).
-   **Ticker de Informações Dinâmico:** Exibe a previsão do tempo para Indaiatuba-SP e a cotação do Dólar/Euro em tempo real, com dados buscados no backend via API.
-   **Design Responsivo:** Interface totalmente adaptável para desktops, tablets e celulares.
-   **Seções Detalhadas:** Apresentação clara dos serviços (IIoT, Automação, Elétrica) e do projeto "Garagem Inteligente".
-   **Otimizado para SEO:** Rotas amigáveis (`/txcar`, `/farol-alto`) para melhor indexação.
-   **Pronto para Produção:** Configurado para deploy com Gunicorn.

---

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python, Flask
-   **Frontend:** HTML5, CSS3, JavaScript
-   **Servidor de Produção (WSGI):** Gunicorn
-   **APIs Externas:**
    -   Open-Meteo para dados climáticos.
    -   AwesomeAPI para cotações de moedas.
-   **Plataforma de Deploy:** Render

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente de desenvolvimento.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/WGuiotti/meu-projeto-flask
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    O servidor de desenvolvimento do Flask será iniciado.
    ```bash
    python app.py
    ```

    Acesse `http://127.0.0.1:5000` em seu navegador.

---

## 📂 Estrutura do Projeto

```
/meu-projeto-flask
├── app.py              # Arquivo principal da aplicação Flask (rotas, lógica)
├── requirements.txt    # Dependências do Python para produção
├── static/             # Arquivos estáticos (CSS, JS, Imagens)
├── templates/          # Arquivos HTML (Jinja2)
└── README.md           # Este arquivo
```

---

## ☁️ Deploy no Render

Este projeto está configurado para deploy na plataforma Render.

-   **Build Command:** `pip install -r requirements.txt`
-   **Start Command:** `gunicorn app:app`

O Render detectará o `requirements.txt` e instalará todas as dependências automaticamente.
