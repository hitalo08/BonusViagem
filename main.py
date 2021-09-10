import os
import pandas as pd
from twilio.rest import Client

account_sid = 'AC8a6e15f1cda4a71ed87a86c10ace9af5'
auth_token = 'bb5b7333c5e65979f11d07cdae4fe1c5'
client = Client(account_sid, auth_token)

lista_meses = ['abril','fevereiro','janeiro','junho','maio','março']
for mes in lista_meses:
    tabela_vendas = pd.read_excel('{}.xlsx'.format(mes))
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print('No mês de {} alguém bateu a meta! Vencedor: {}, Vendas: {}'.format(mes,vendedor,vendas))
        message = client.messages.create(
            to='+55 11984617216',
            from_='+15039173990',
            body='No mês de {} alguém bateu a meta! Vencedor: {}, Vendas: {}'.format(mes,vendedor,vendas))
        print(message.sid)



