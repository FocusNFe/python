# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "http://homologacao.acrasnfe.acras.com.br/v2/nfe"

# Substituir pela sua identificação interna da nota
ref = {"ref":"12345"}

token="token_enviado_pelo_suporte"
 
'''
Usamos dicionarios para armazenar os campos e valores que em seguida,
serao convertidos em JSON e enviados para nossa API
'''
nfe = {}
itens = {}
notas_referenciadas ={}

nfe["natureza_operacao"] = "Venda"
nfe["forma_pagamento"] = "0"
nfe["data_emissao"] = "2018-03-07T10:20:00-03:00"
nfe["tipo_documento"] = "0"
nfe["local_destino"] = "1"
nfe["finalidade_emissao"] = "4"
nfe["consumidor_final"] = "0"
nfe["presenca_comprador"] = "9"
nfe["cnpj_emitente"] = "99999999999999"
nfe["logradouro_emitente"] = "R. Padre Pigato"
nfe["numero_emitente"] = "9236"
nfe["bairro_emitente"] = "Santa Gula"
nfe["municipio_emitente"] = "Curitiba"
nfe["uf_emitente"] = "PR"
nfe["cep_emitente"] = "82320999"
nfe["telefone_emitente"] = "4199999999"
nfe["inscricao_estadual_emitente"] = "999999999"
nfe["regime_tributario_emitente"] = "1"
nfe["cpf_destinatario"] = "99999999999"
nfe["nome_destinatario"] = "NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
nfe["logradouro_destinatario"] = "Rua Prof. Yolanda Romeu Lugarini"
nfe["numero_destinatario"] = "1"
nfe["bairro_destinatario"] = "JD SANTA CECILIA"
nfe["municipio_destinatario"] = "CAMPO MAGRO"
nfe["uf_destinatario"] = "PR"
nfe["cep_destinatario"] = "83000000"
nfe["indicador_inscricao_estadual_destinatario"] = "2"
nfe["icms_base_calculo"] = "0"
nfe["icms_valor_total"] = "0"
nfe["icms_valor_total_desonerado"] = "0"
nfe["icms_base_calculo_st"] = "0"
nfe["icms_valor_total_st"] = "0"
nfe["valor_produtos"] = "1.00"
nfe["valor_frete"] = "0"
nfe["valor_seguro"] = "0"
nfe["valor_desconto"] = "0"
nfe["valor_total_ii"] = "0"
nfe["valor_ipi"] = "0"
nfe["valor_pis"] = "0"
nfe["valor_cofins"] = "0"
nfe["valor_outras_despesas"] = "0"
nfe["valor_total"] = "1.00"
nfe["modalidade_frete"] = "0"
notas_referenciadas["chave_nfe"] = 41170599999999999999550020000001111337477298
itens["numero_item"] = "1"
itens["codigo_produto"] = "ESSP"
itens["descricao"] = "Carrinho de corrida"
itens["cfop"] = "1202"
itens["unidade_comercial"] = "UN"
itens["quantidade_comercial"] = "1.00"
itens["valor_unitario_comercial"] = "1.00"
itens["valor_bruto"] = "1.00"
itens["valor_desconto"] = "0"
itens["unidade_tributavel"] = "UN"
itens["codigo_ncm"] = "49119900"
itens["quantidade_tributavel"] = "1.00"
itens["valor_unitario_tributavel"] = "1.00"
itens["inclui_no_total"] = "1"
itens["icms_origem"] = "0"
itens["icms_situacao_tributaria"] = "103"
itens["pis_situacao_tributaria"] = "99"
itens["cofins_situacao_tributaria"] = "99"

# Adicionamos os dados das variaveis itens e notas_referenciadas como listas ao dicionario principal.
nfe["items"] = [itens]
nfe["notas_referenciadas"] = [notas_referenciadas]

r = requests.post(url, params=ref, data=json.dumps(nfe), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API
print(r.status_code, r.text)