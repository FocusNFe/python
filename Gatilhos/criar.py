# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "http://homologacao.acrasnfe.acras.com.br/v2/hooks"

token="token_enviado_pelo_suporte"

'''
Usamos um dicionario para armazenar os campos e valores que em seguida,
serao convertidos a JSON e enviados para nossa API
'''
dados = {}
dados["cnpj"] = "51916585000125"
dados["event"] = "nfe"
dados["url"] = "http://minha.url/nfe"

r = requests.post(url, data=json.dumps(dados), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)