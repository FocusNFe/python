# Faça o download e instalação da biblioteca requests, através do python-pip.
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "https://homologacao.focusnfe.com.br/v2/nfce/"

# Substituir pela sua identificação interna da nota
ref = "1234"

token="token_enviado_pelo_suporte"

# Use este parametro para obter mais informacoes em suas consultas
completa = "completa=1"

r = requests.get(url+ref, params=completa, auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)
