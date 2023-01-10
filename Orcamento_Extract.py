import requests
import datetime
from time import strptime
import getpass

import pandas as pd
import re

#Define o token gerado pelo portal da transparência para acessar a API
token = getpass.getpass()

#Lê as listas de empenhos, separadas por UG
ne_160_list = pd.read_excel('/Empenhos_160.xlsx')
ne_160_list = ne_160_list['EMPENHOS'].to_list()
ne_167_list = pd.read_excel('/Empenhos_167.xlsx')
ne_167_list = ne_167_list['EMPENHOS'].to_list()

#Acessa os dados através da API e salva em um DataFrame
ne_160_df = pd.DataFrame()

for emp in ne_160_list:
    data = requests.get(
    f'https://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos/16029700001{emp}',
    headers={"chave-api-dados":token}
    )
    data_df = data.json()
    data_df = pd.json_normalize(data_df)
    ne_160_df = pd.concat([ne_160_df,data_df])

ne_167_df = pd.DataFrame()

for emp in ne_list:
    data = requests.get(
    f'https://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos/16729700001{emp}',
    headers={"chave-api-dados":token}
    )
    data_df = data.json()
    data_df = pd.json_normalize(data_df)
    ne_167_df = pd.concat([ne_167_df,data_df])
    
#Filtra as colunas que nos interessam
ne_160_df = ne_160_df[[
       'data', 'documento', 'documentoResumido', 'observacao',
       'favorecido', 'codigoFavorecido', 'nomeFavorecido',
       'valor', 'codigoUg','numeroProcesso',
]]

ne_167_df = ne_167_df[[
       'data', 'documento', 'documentoResumido', 'observacao',
       'favorecido', 'codigoFavorecido', 'nomeFavorecido',
       'valor', 'codigoUg','numeroProcesso',
]]

#Extrai a NC da observação
ne_160_df['NC'] = ne_160_df['observacao'].apply(
    lambda row: re.findall('(nc+\d{1,6})|(NC+\d{1,6})',row)
    )
ne_160_df['NC'] = ne_160_df['NC'].apply(
    lambda row: row[0][-1] if len(row) > 0 else 'Na'
    )
ne_160_df['NC'] = ne_160_df['NC'].apply(
    lambda row: row.split('NC')[-1] if row != '' else 'Na'
    )

ne_167_df['NC'] = ne_167_df['observacao'].apply(
    lambda row: re.findall('(nc+\d{1,6})|(NC+\d{1,6})',row)
    )
ne_167_df['NC'] = ne_167_df['NC'].apply(
    lambda row: row[0][-1] if len(row) > 0 else 'Na'
    )
ne_167_df['NC'] = ne_167_df['NC'].apply(
    lambda row: row.split('NC')[-1] if row != '' else 'Na'
    )
    
#Limpa os valores e faz o typecast para float
ne_160_df['valor'] = ne_160_df['valor'].apply(
    lambda num: f'{num.split(".")[0]}{num.split(".")[-1]}' if len(num.split(".")) > 1 else num
)
ne_160_df['valor'] = ne_160_df['valor'].apply(
    lambda num: num.replace(',','.')
)
ne_160_df = ne_160_df.astype({
    'valor':float
})

ne_167_df['valor'] = ne_167_df['valor'].apply(
    lambda num: f'{num.split(".")[0]}{num.split(".")[-1]}' if len(num.split(".")) > 1 else num
)
ne_167_df['valor'] = ne_167_df['valor'].apply(
    lambda num: num.replace(',','.')
)
ne_167_df = ne_167_df.astype({
    'valor':float
})

#Define função para acessar docs de liquidação e pagamento através de API
def check_relations (token: str, codNe: str):
  doc = requests.get(
    'https://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos-relacionados',
    headers={"chave-api-dados":token},
    params={'codigoDocumento':codNe,'fase':1}
    )
  doc_df = doc.json()
  doc_df = pd.json_normalize(doc_df)
  if len(doc_df.axes[0]) == 0:
    pass
  else: 
    doc_df = doc_df[['data','fase','documento']]
    doc_df = doc_df.rename(columns={'data':'data_relac', 'documento':'documento_relac'})
    doc_df['documento'] = codNe
    return doc_df
  
  #Checa os documentos de liq e pag e os anexa ao df principal
check_liq=pd.DataFrame()

for ne in ne_160_df['documento']:
  df = check_relations(token,ne)
  check_liq = pd.concat([check_liq,df])

check_ns = check_liq[check_liq['fase'] =='Liquidação']
check_ns["LIQ"] = 1
check_ns = check_ns.rename(columns={'data_relac':'data_liq'})
check_ns = check_ns[['documento','data_liq','LIQ']]
check_ns = check_ns.drop_duplicates(subset=['documento'])

check_ob = check_liq[check_liq['fase'] =='Pagamento']
check_ob["PAG"] = 1
check_ob = check_ob.rename(columns={'data_relac':'data_pag'})
check_ob = check_ob[['documento','data_pag','PAG']]
check_ob = check_ob.drop_duplicates(subset=['documento'])

ne_160_df = ne_160_df.merge(
    check_ns, on='documento', how='left', suffixes=(False, '_liq')
    )

ne_160_df = ne_160_df.merge(
    check_ob, on='documento', how='left', suffixes=(False, '_pag')
    )
    
check_liq=pd.DataFrame()

for ne in ne_167_df['documento']:
  df = check_relations(token,ne)
  check_liq = pd.concat([check_liq,df])

check_ns = check_liq[check_liq['fase'] =='Liquidação']
check_ns["LIQ"] = 1
check_ns = check_ns.rename(columns={'data_relac':'data_liq'})
check_ns = check_ns[['documento','data_liq','LIQ']]
check_ns = check_ns.drop_duplicates(subset=['documento'])

check_ob = check_liq[check_liq['fase'] =='Pagamento']
check_ob["PAG"] = 1
check_ob = check_ob.rename(columns={'data_relac':'data_pag'})
check_ob = check_ob[['documento','data_pag','PAG']]
check_ob = check_ob.drop_duplicates(subset=['documento'])

ne_167_df = ne_167_df.merge(
    check_ns, on='documento', how='left', suffixes=(False, '_liq')
    )

ne_167_df = ne_167_df.merge(
    check_ob, on='documento', how='left', suffixes=(False, '_pag')
    )
    
#Transforma as datas em datetime e calcula o tempo de liq e pag
ne_160_df['data'] = pd.to_datetime(ne_160_df['data'],dayfirst=True)
ne_160_df['data_liq'] = pd.to_datetime(
    ne_160_df['data_liq'],dayfirst=True
    )
ne_160_df['data_pag'] = pd.to_datetime(
    ne_160_df['data_pag'],dayfirst=True
    )

ne_160_df['tempo_liq'] = (ne_160_df['data'] - ne_160_df['data_liq'])
ne_160_df['tempo_pag'] = (ne_160_df['data_liq'] - ne_160_df['data_pag'])

ne_167_df['data'] = pd.to_datetime(ne_167_df['data'],dayfirst=True)
ne_167_df['data_liq'] = pd.to_datetime(
    ne_167_df['data_liq'],dayfirst=True
    )
ne_167_df['data_pag'] = pd.to_datetime(
    ne_167_df['data_pag'],dayfirst=True
    )

ne_167_df['tempo_liq'] = (ne_167_df['data'] - ne_167_df['data_liq'])
ne_167_df['tempo_pag'] = (ne_167_df['data_liq'] - ne_167_df['data_pag'])

#Define função para extrair as UGR
def def_ugr (var: str):
  ugr = ()
  if "DGP" in var:
    ugr = "DGP"
  elif "FEX" in var:
    ugr = "FEX"
  elif "COLOG" in var:
    ugr = "COLOG"
  elif "COTER" in var:
    ugr = "COTER"
  elif "DECEX" in var:
    ugr = "DECEX"
  elif "DGO" in var:
    ugr = "DGO"
    
  return ugr

#Define as UGR
ne_160_df['UGR'] = ne_160_df['observacao'].apply(
    lambda row:
    def_ugr(row)
)

ne_167_df['UGR'] = ne_167_df['observacao'].apply(
    lambda row:
    def_ugr(row)
)

#Lê as lista de NCs
nc_160_df = pd.read_excel('/Creditos_160.xlsx')
nc_160_df = nc_160_df.rename(columns={'CREDITOS':'NR'})
nc_167_df = pd.read_excel('/content/drive/MyDrive/EB/Creditos_167.xlsx')
nc_167_df = nc_167_df.rename(columns={'CREDITOS':'NR'})

#Lê os dados das Notas de Créditos extraídos do Portal da Transparência
credito_df = pd.read_csv('/content/drive/MyDrive/EB/Notas_de_Credito.csv')

credito_df = credito_df[[
    'UGFAV', 'UGR', 'PTRES', 'ND', 'PI', 'DATA',
       'NR', 'VALOR', 'OBS'
]]
