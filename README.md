<div align="center">
  <img src="static/img/logo.jpg" alt="GuIIOTTI Logo" width="150">
  <h1>GuIIOTTI - Institutional Website</h1>
  <p>
    <strong>
      <a href="#-guiiotti---institutional-website">English</a> | 
      <a href="#-guiiotti---website-institucional-português">Português</a>
    </strong>
  </p>
</div>

Institutional website and portfolio for **GuIIOTTI - IIoT & Automation Solutions**, developed with Flask. The site showcases the company's services, contact information, and dynamic features.

**[➡️ Access the live version here](https://guiiotti.onrender.com/)**

> **⚠️ Important Note about Hosting:**
> This project is hosted on Render's "Free Tier". Consequently, the server goes into hibernation mode after 15 minutes of inactivity to conserve resources.
>
> **When accessing the link for the first time, you may need to wait about 50 seconds to 1 minute for the application to "wake up" and load.** Thank you for your patience!

---

## ✨ Key Features

-   **Multi-language:** Full support for Portuguese (🇧🇷), English (🇬🇧), and Spanish (🇪🇸).
-   **Dynamic Info Ticker:** Displays weather forecast for Indaiatuba-SP and Dollar/Euro exchange rates in real-time, fetching data from the backend via API.
-   **Responsive Design:** Interface fully adaptable for desktops, tablets, and mobile phones.
-   **Detailed Sections:** Clear presentation of services (IIoT, Automation, Electrical) and the "Smart Garage" project.
-   **SEO Optimized:** Friendly routes (`/txcar`, `/farol-alto`) for better indexing.
-   **Production Ready:** Configured for deployment with Gunicorn.

---

## 🛠️ Technologies Used

-   **Backend:** Python, Flask
-   **Frontend:** HTML5, CSS3, JavaScript
-   **Production Server (WSGI):** Gunicorn
-   **External APIs:**
    -   Open-Meteo for weather data.
    -   AwesomeAPI for currency exchange rates.
-   **Deployment Platform:** Render

---

## 💻 Detailed Development Guide

This section provides detailed instructions to set up the environment, understand the structure, and contribute to the project.

### Prerequisites

*   **Python 3.10+**: Ensure Python is installed.
*   **Git**: For version control.
*   **Virtualenv**: Recommended to isolate project dependencies.

### Installation Steps

1.  **Clone the Repository**
    Download the source code to your local machine:
    ```bash
    git clone https://github.com/WGuiotti/meu-projeto-flask
    cd meu-projeto-flask
    ```

2.  **Virtual Environment Setup (Venv)**
    It is good practice to create an isolated environment to avoid conflicts with other system libraries.
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux (Bash)
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Install all libraries listed in `requirements.txt` (Flask, Requests, Gunicorn, etc.):
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Run in Development Mode**
    Start the local server. `debug=True` mode is enabled in the code, allowing "hot-reload" (automatic update when saving files).
    ```bash
    python app.py
    ```

    📍 Access in your browser: `http://127.0.0.1:5000`

---

## 📂 Understanding the File Structure

Below, we detail the function of each main directory and file to facilitate code navigation:

```
/meu-projeto-flask
├── app.py                  # 🧠 Application brain. Contains routes, backend logic, API calls, and translation dictionary.
├── requirements.txt        # 📦 List of packages required for Render/Production to install the project.
├── static/                 # 🎨 Public static files:
│   ├── css/                # Stylesheets (style.css).
│   ├── img/                # Images, logos, and animated GIFs.
│   └── js/                 # JavaScript scripts for the frontend.
├── templates/              # 📄 HTML templates rendered by Jinja2:
│   ├── index.html          # Main page (Landing Page).
│   └── pages/              # Secondary pages (About, Services).
└── README.md               # 📖 Project documentation.
```

---

## ☁️ Deploy on Render

This project is configured for deployment on the Render platform.

-   **Build Command:** `pip install -r requirements.txt`
-   **Start Command:** `gunicorn app:app`

Render will detect `requirements.txt` and install all dependencies automatically.

<br><br>

---
---

<br><br>

# 🇧🇷 GuIIOTTI - Website Institucional (Português)

Website institucional e portfólio para a **GuIIOTTI - Soluções em IIoT & Automação**, desenvolvido com Flask. O site apresenta os serviços da empresa, informações de contato e funcionalidades dinâmicas.

**➡️ Acesse a versão ao vivo aqui**

> **⚠️ Nota Importante sobre a Hospedagem:**
> Este projeto está hospedado no plano gratuito ("Free Tier") do Render. Devido a isso, o servidor entra em modo de hibernação após 15 minutos de inatividade para economizar recursos.
>
> **Ao acessar o link pela primeira vez, pode ser necessário aguardar cerca de 50 segundos a 1 minuto para que a aplicação "acorde" e carregue.** Agradecemos a paciência!

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

## 💻 Guia de Desenvolvimento Detalhado

Esta seção fornece instruções detalhadas para configurar o ambiente, entender a estrutura e contribuir com o projeto.

### Pré-requisitos

*   **Python 3.10+**: Certifique-se de ter o Python instalado.
*   **Git**: Para controle de versão.
*   **Virtualenv**: Recomendado para isolar as dependências do projeto.

### Passo a Passo de Instalação

1.  **Clonagem do Repositório**
    Baixe o código fonte para sua máquina local:
    ```bash
    git clone https://github.com/WGuiotti/meu-projeto-flask
    cd meu-projeto-flask
    ```

2.  **Configuração do Ambiente Virtual (Venv)**
    É uma boa prática criar um ambiente isolado para não conflitar com outras bibliotecas do seu sistema.
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux (Bash)
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalação de Dependências**
    Instale todas as bibliotecas listadas no `requirements.txt` (Flask, Requests, Gunicorn, etc.):
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Execução em Modo de Desenvolvimento**
    Inicie o servidor local. O modo `debug=True` está ativado no código, o que permite "hot-reload" (atualização automática ao salvar arquivos).
    ```bash
    python app.py
    ```

    📍 Acesse em seu navegador: `http://127.0.0.1:5000`

---

## 📂 Entendendo a Estrutura de Arquivos

Abaixo, detalhamos a função de cada diretório e arquivo principal para facilitar a navegação no código:

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
