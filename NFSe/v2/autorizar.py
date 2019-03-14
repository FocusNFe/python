# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "https://homologacao.focusnfe.com.br/v2/nfse"

# Substituir pela sua identificação interna da nota
ref = {"ref":"12345"}

token="token_enviado_pelo_suporte"
 
'''
Usamos dicionarios para armazenar os campos e valores que em seguida,
serao convertidos em JSON e enviados para nossa API
'''
nfse = {}
nfse["prestador"] = {}
nfse["servico"] = {}
nfse["tomador"] = {}
nfse["tomador"]["endereco"] = {}

nfse["razao_social"] = "ACME INK"
nfse["data_emissao"] = "2018-02-26T12:00:00-03:00"
nfse["incentivador_cultural"] =  "false"
nfse["natureza_operacao"] = "1"
nfse["optante_simples_nacional"] = "true"
nfse["status"] = "1"
nfse["prestador"]["cnpj"] = "99999999999999"
nfse["prestador"]["inscricao_municipal"] = "99999999"
nfse["prestador"]["codigo_municipio"] = "9999999"
nfse["servico"]["aliquota"] = "2.92"
nfse["servico"]["base_calculo"] = "1.00"
nfse["servico"]["discriminacao"] = "SERVICOS E MAO DE OBRA"
nfse["servico"]["iss_retido"] = "0"
nfse["servico"]["item_lista_servico"] = "1412"
nfse["servico"]["valor_iss"] = "11.68"
nfse["servico"]["valor_liquido"] = "1.00"
nfse["servico"]["valor_servicos"] = "1.00"
nfse["tomador"]["cnpj"] = "99999999999999"
nfse["tomador"]["razao_social"] = "Parkinson da silva coelho JR"
nfse["tomador"]["endereco"]["bairro"] = "São Miriti"
nfse["tomador"]["endereco"]["cep"] = "31999-000"
nfse["tomador"]["endereco"]["codigo_municipio"] = "9999999"
nfse["tomador"]["endereco"]["logradouro"] = "João Batista Netos"
nfse["tomador"]["endereco"]["numero"] = "34"
nfse["tomador"]["endereco"]["uf"] = "MG"

#print (json.dumps(nfse))
r = requests.post(url, params=ref, data=json.dumps(nfse), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)
