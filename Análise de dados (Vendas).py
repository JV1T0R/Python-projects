'''
Desafio do canal da hashtag treinamentos
Link da playlist: https://www.youtube.com/playlist?list=PLpdAy0tYrnKyCZsE-ifaLV1xnkXBE9n7T 
'''

import os
import pandas as pd

lista_arquivo = os.listdir("C:/Users/Desktop/Documents/análise_de_dados/Vendas")
tabela_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:/Users/Desktop/Documents/análise_de_dados/Vendas/{arquivo}")
        tabela_total = tabela_total._append(tabela)
        tabela_produtos = tabela_total.groupby("Produto").sum()
        tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
        tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
        tabela_faturamento = tabela_total.groupby("Produto").sum
        tabela_faturamento = tabela_faturamento(["Faturamento"]).sort_values(by="Faturamento", ascending=False)
        tabela_lojas = tabela_total.groupby("Loja").sum
        tabela_lojas = tabela_lojas(["Faturamento"])

print(tabela_lojas)
