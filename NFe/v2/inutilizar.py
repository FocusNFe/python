# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
''' 
url = "https://homologacao.focusnfe.com.br/v2/nfe/inutilizacao"

token="token_enviado_pelo_suporte"

'''
Usamos um dicionario para armazenar os campos e valores que em seguida,
serao convertidos a JSON e enviados para nossa API
'''
inutilizacao={}
inutilizacao["cnpj"] = "CNPJ da empresa emitente"
inutilizacao["serie"] = "Serie da numeracao da NFCe que tera uma faixa de numeracao inutilizada"
inutilizacao["numero_inicial"] = "Numero inicial a ser inutilizado"
inutilizacao["numero_final"] = "Numero final a ser inutilizado"
inutilizacao["justificativa"] = "Justificativa da inutilizacao (minimo 15 caracteres)"

r = requests.post(url, data=json.dumps(inutilizacao), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)
