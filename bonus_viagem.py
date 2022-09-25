import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC00c8d1e6e9362eb8313666ad8c801cf4"
# Your Auth Token from twilio.com/console
auth_token  = "fa0cd1ee50b0ae35b8a4378ae60fb757"
client = Client(account_sid, auth_token)

# Instalar : Pandas ( integração com excel) , Openpyxl (integração com excel) e Twilio (integração com sms)

# Passo a passo de solução

# Abrir os 6 arquivos em excel

lista_meses = ['janeiro', 'fevereiro', 'março' , 'abril' , 'maio', 'junho']

for mes in lista_meses :
       tabela_vendas = pd.read_excel(f'{mes}.xlsx')
       if (tabela_vendas['Vendas'] > 55000).any() : 
            vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
            vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
            print(f' No mes {mes} alguém bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')
            message = client.messages.create(
                to="+5531973132953", 
                from_="+12562739967",
                body= f' No mes {mes} alguém bateu a meta. Vendedor: {vendedor} , Vendas: {vendas}')

            print(message.sid)




# Para cada arquivo:

# Verificar se algum valor na coluna venda daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> envia um sms com o Nome ,o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não quero fazer nada

