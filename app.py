import requests
from bs4 import BeautifulSoup
from flask import Flask,jsonify
from flask_cors import CORS

def tratar(str):
    try:
        a = str.replace('.', '').replace(',', '.').replace('%', '')
        return float(a)

    except (ValueError, AttributeError):
        return float('inf')
    
def buscar_dados_fiis():
    url = 'https://fundamentus.com.br/fii_resultado.php'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        tabela = soup.find_all('table')

        if tabela:
            tabela_principal = tabela[0]
            linhas = tabela_principal.find('tbody').find_all('tr')
            lista_fii = []

            for linha in linhas:
                celulas = linha.find_all('td')

                if len(celulas) > 9:
                    papel = celulas[0].text
                    segmento = celulas[1].text
                    cotacao = celulas[2].text
                    ffo_yield = celulas[3].text
                    div_yield = celulas[4].text
                    pvp = celulas[5].text
                    valor_mercado = celulas[6].text
                    liquidez = celulas[7].text
                    qtd_imoveis = celulas[8].text
                    vacancia = celulas[9].text

                    fii_info = {
                        'Papel': papel,
                        'Segmento': segmento,
                        'Cotacao': cotacao,
                        'FFO Yield': ffo_yield,
                        'Dividend Yield': div_yield,
                        'P/VP': pvp,
                        'Valor de Mercado': valor_mercado,
                        'Liquidez': liquidez,
                        'Qtd de imoveis': qtd_imoveis,
                        'Vacancia Media': vacancia
                    }

                    lista_fii.append(fii_info)


    fii_ordem_DY=sorted(lista_fii,key=lambda fii:tratar(fii["Dividend Yield"]))
    for i,fii in enumerate(fii_ordem_DY):
        fii['Raking_DY']=i+1

    fii_ordem_PVP=sorted(lista_fii,key=lambda fii:tratar(fii["P/VP"]))
    for i,fii in enumerate(fii_ordem_PVP):
        fii['Raking_PVP']=i+1

    for fii in lista_fii:
        fii["metodo"]=fii['Raking_DY']+fii["Raking_PVP"]


    lista_final= sorted(lista_fii,key=lambda fii:fii['metodo'])

    return lista_final
        
app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "<h1>API Raking de FIIs</h1><p>Acesse /fiis para ver os dados</p>"

@app.route('/fiis')
def get_fiis():
    dados=buscar_dados_fiis()
    return jsonify(dados)

if __name__== "__main__":
    app.run()