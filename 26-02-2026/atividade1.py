import datetime
""".datetime.now()"""
print(f"estaio nota {9+1}")

data_atual = datetime.datetime.now()

dia = data_atual.day
mes = data_atual.month
ano = data_atual.year




"""idade = int(input("Digite sua idade \n"))
print(f" Voce deve ter nascido em {2026 - idade} ou em {2025 - idade}") """



idade_dia = int(input("Digite o DIA que nasceu"))
idade_mes = int(input("Digite o MES que nasceu"))
idade_ano = int(input("Digite o ANO que nasceu"))

""" 
if idade_dia < dia and idade_mes < mes and idade_ano < ano:
    
    print(f" Voce deve ter nascido em {} ") 
"""

"""Posteriomente fazer validação com a função DateTime"""