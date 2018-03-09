# Faça o download e instalação da biblioteca requests, através do python-pip.
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "http://homologacao.acrasnfe.acras.com.br/v2/hooks/"

token="token_enviado_pelo_suporte"

hook_id = "Vj5rmkBq"

r = requests.delete(url+hook_id, auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)