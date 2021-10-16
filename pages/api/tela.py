import requests
from datetime import datetime, timedelta
from datetime import date
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,CAD-BRL,NZD-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar_usa = requisicao_dic['USDBRL']['bid']
    cotacao_dolar_cad = requisicao_dic['CADBRL']['bid']
    cotacao_dolar_nz = requisicao_dic['NZDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    
    texto = f'''   
    Dólar (USA): {cotacao_dolar_usa}
    Dólar (Canadá): {cotacao_dolar_cad}
    Dólar (Nova Zelândia): {cotacao_dolar_nz}
    Euro: {cotacao_euro}
    BTC (Bitcoin): {cotacao_btc}'''

    texto_resposta["text"] = texto


janela = Tk()
janela.title("Cotação Atual de Moedas")
janela.geometry("400x400")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=70, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=50, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=40, pady=10)


janela.mainloop()