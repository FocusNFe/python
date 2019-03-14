# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "https://homologacao.focusnfe.com.br/v2/nfce"

# Substituir pela sua identificação interna da nota
ref = {"ref":"1234"}

token="token_enviado_pelo_suporte"
 
'''
Usamos dicionarios para armazenar os campos e valores que em seguida,
serao convertidos em JSON e enviados para nossa API
'''
nfce = {}
items = {}
formas_pagamento={}

nfce["cnpj_emitente"] = "99999999999999"
nfce["nome_emitente"] = "Acme ink"
nfce["nome_fantasia_emitente"] = "Acme ink"
nfce["logradouro_emitente"] = "Rua Tupiniquim"
nfce["numero_emitente"] = "4000"
nfce["bairro_emitente"] = "Brás"
nfce["municipio_emitente"] = "São Paulo"
nfce["uf_emitente"] = "SP"
nfce["cep_emitente"] = "99997-000"
nfce["inscricao_estadual_emitente"] = "111111111"
nfce["data_emissao"] = "2018-03-06T17:11:00.939-03:00"
nfce["natureza_operacao"] = "Venda ao Consumidor"
nfce["tipo_documento"] = "1"
nfce["presenca_comprador"] = "1"
nfce["finalidade_emissao"] = "1"
nfce["modalidade_frete"] = "9"
nfce["forma_pagamento"] = "0"
nfce["nome_destinatario"] = "NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
nfce["cpf_destinatario"] = "99999999999"
nfce["informacoes_adicionais_contribuinte"] = "Informacoes adicionais do contribuinte"
nfce["valor_produtos"] = "15.0"
nfce["valor_desconto"] = "0.00"
nfce["valor_total"] = "15.0"
formas_pagamento["forma_pagamento"] = "4"
formas_pagamento["valor_pagamento"] = "15.00"
formas_pagamento["bandeira_operadora"] = "7"
formas_pagamento["troco"] = "0"
itens["numero_item"] = "1"
itens["codigo_produto"] = "353"
itens["descricao"] = "NOTA FISCAL EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
itens["codigo_ncm"] = "48024090"
itens["cfop"] = "5102"
itens["valor_desconto"] = "0.00"
itens["icms_origem"] = "0"
itens["icms_situacao_tributaria"] = "400"
itens["unidade_comercial"] = "UN"
itens["unidade_tributavel"] = "UN"
itens["quantidade_comercial"] = "10"
itens["quantidade_tributavel"] = "10"
itens["valor_unitario_comercial"] = "1.5"
itens["valor_unitario_tributavel"] = "1.5"
itens["valor_bruto"] = "15.00"

# Adicionamos os dados das variaveis itens e formas_pagamento como listas ao dicionario principal.
nfce["items"] = [itens]
nfce["formas_pagamento"] = [formas_pagamento]

r = requests.post(url, params=ref, data=json.dumps(nfce), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)
