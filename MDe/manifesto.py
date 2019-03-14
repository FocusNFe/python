# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "https://homologacao.focusnfe.com.br/v2/nfes_recebidas/"

token="token_enviado_pelo_suporte"

chave = "chave_da_nota_fiscal"

'''
Usamos um dicionario para armazenar os campos e valores que em seguida,
serao convertidos a JSON e enviados para nossa API
'''
manifesto = {}
manifesto["tipo"] = "ciencia"

r = requests.post(url+chave+"/manifesto", data=json.dumps(manifesto), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)
