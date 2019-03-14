# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
''' 
url = "https://homologacao.focusnfe.com.br/v2/cte/inutilizacao"

token="Token_enviado_pelo_suporte"

'''
Usamos um dicionario para armazenar os campos e valores que em seguida,
serao convertidos a JSON e enviados para nossa API.
'''
inutilizacao={}
inutilizacao["cnpj"] = "51916585000125"
inutilizacao["serie"] = "1"
inutilizacao["numero_inicial"] = "1"
inutilizacao["numero_final"] = "3"
inutilizacao["justificativa"] = "Justificativa da inutilizacao minimo 15 caracteres"
inutilizacao["modelo"] = "67"

r = requests.post(url, data=json.dumps(inutilizacao), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API.
print(r.status_code, r.text)
