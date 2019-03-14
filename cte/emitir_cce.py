# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "https://homologacao.focusnfe.com.br/v2/cte/"

# Substituir pela sua identificação interno do CTe.
ref = "12345"

token="Token_enviado_pelo_suporte"

'''
Usamos um dicionario para armazenar os campos e valores que em seguida,
serao convertidos a JSON e enviados para nossa API.
'''
cce = {"campo_corrigido": "uf_inicio", "valor_corrigido": "PR"}

r = requests.post(url+ref+"/carta_correcao", data=json.dumps(cce), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API.
print(r.status_code, r.text)
