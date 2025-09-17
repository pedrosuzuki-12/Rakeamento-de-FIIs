#  Analisador de Fundos Imobiliários (FIIs)

Uma aplicação web que extrai dados de Fundos Imobiliários (FIIs) em tempo real do site Fundamentus, classifica os ativos com base em um ranking customizado e apresenta os resultados em uma interface interativa que permite a filtragem a gosto do usuário.

---

## ✨ Funcionalidades

*   **Web Scraping:** Extração de dados de todos os FIIs listados no site Fundamentus utilizando Python com as bibliotecas **`Requests`** e **`BeautifulSoup`**.
*   **API RESTful:** O backend, desenvolvido com **`Flask`**, fornece os dados extraídos através de um endpoint (`/fiis`).
*   **Ranking Customizado:** Os FIIs são classificados com base na soma de suas posições nos rankings de *Dividend Yield* e *P/VP* (Preço sobre Valor Patrimonial), priorizando ativos com bom equilíbrio entre os dois indicadores.
*   **Filtragem Dinâmica:** Interface interativa que permite ao usuário filtrar os FIIs em tempo real por Liquidez Mínima, Dividend Yield Mínimo e P/VP Mínimo.

---

## 🛠️ Tecnologias Utilizadas

### Backend
*   **Python 3.8+**
*   **Flask:** Micro-framework para a criação da API.
*   **Flask-CORS:** Para permitir requisições do frontend.
*   **BeautifulSoup4:** Para a análise do HTML e extração dos dados.
*   **Requests:** Para realizar as requisições HTTP ao site.

### Frontend
*   **HTML5:** Estrutura da página.
*   **CSS3:** Estilização da interface.
*   **JavaScript (ES6):** Para consumir a API, manipular o DOM e aplicar os filtros.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar a aplicação localmente.

### Pré-requisitos
*   **Python 3.8+**
*   **pip** (gerenciador de pacotes do Python)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO/NOME_DO_SEU_REPOSITORIO.git
    cd NOME_DO_SEU_REPOSITORIO
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o servidor Flask (Backend):**
    ```bash
    python app.py
    ```
    O servidor estará rodando em `http://127.0.0.1:5000`.

4.  **Abra a interface (Frontend):**
    Abra o arquivo `index.html` diretamente no seu navegador de preferência (ex: Google Chrome, Firefox). A aplicação deve carregar os dados automaticamente.

---

## 🧠 Lógica do Ranking

O método de ranking busca identificar FIIs que apresentam um bom equilíbrio entre geração de renda (*Dividend Yield*) e um preço que não esteja excessivamente caro (*P/VP*).

1.  **Ranking de Dividend Yield (DY):** Os FIIs são ordenados do maior para o menor DY. A melhor posição (maior DY) recebe o ranking **1**.
2.  **Ranking de P/VP:** Os FIIs são ordenados do menor para o maior P/VP. A melhor posição (menor P/VP) recebe o ranking **1**.
3.  **Ranking Final:** É calculado somando a posição do FII em cada um dos rankings (`Ranking_DY + Ranking_PVP`). O objetivo é encontrar os FIIs com a menor soma, indicando uma boa classificação em ambos os critérios simultaneamente.

---

## 👨‍💻 Autor

Feito por **Pedro Vitor Suzuki Lau**.
