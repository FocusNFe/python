# Faça o download e instalação da biblioteca requests, através do python-pip.
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "https://homologacao.focusnfe.com.br/v2/nfes_recebidas/"

token="token_enviado_pelo_suporte"

chave = "chave_da_nota_fiscal"

r = requests.get(url+chave+"/carta_correcao.xml", auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)
