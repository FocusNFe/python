# Faça o download e instalação da biblioteca requests, através do python-pip.
import json
import requests

''' 
Para ambiente de produção use a variável abaixo:
url = "https://api.focusnfe.com.br"
'''
url = "http://homologacao.acrasnfe.acras.com.br/v2/cte_os"

# Substituir pela sua identificação interno do CTe.
ref = {"ref":"12345"}

token="Token_enviado_pelo_suporte"
 
'''
Usamos dicionarios para armazenar os campos e valores que em seguida,
serao convertidos em JSON e enviados para nossa API.
'''
cte_os = {}
seguros_carga = {}
documentos_referenciados ={}

cte_os["bairro_emitente"] = "S\u00e3o Cristov\u00e3o"
cte_os["bairro_tomador"] = "Bacacheri"
cte_os["cep_emitente"] = "99880077"
cte_os["cep_tomador"] = "88991188"
cte_os["cfop"] = "5353"
cte_os["cnpj_emitente"] = "51916585000125"
cte_os["cnpj_tomador"] = "51966818092777"
cte_os["codigo_municipio_emitente"] = "2927408"
cte_os["codigo_municipio_envio"] = "5200050"
cte_os["codigo_municipio_fim"] = "3100104"
cte_os["codigo_municipio_inicio"] = "5200050"
cte_os["codigo_municipio_tomador"] = "4106902"
cte_os["codigo_pais_tomador"] = "1058"
cte_os["complemento_emitente"] = "Andar 19 - sala 23"
cte_os["data_emissao"] = "2018-06-18T09:17:00"
cte_os["descricao_servico"] = "Descricao do seu servico aqui"
documentos_referenciados["data_emissao"] = "2018-06-10"
documentos_referenciados["numero"] = "1"
documentos_referenciados["serie"] = "1"
documentos_referenciados["subserie"] = "1"
documentos_referenciados["valor"] = "1.00"
cte_os["funcionario_emissor"] = "Nome do funcionario que fez a emissao"
cte_os["icms_aliquota"] = "17.00"
cte_os["icms_base_calculo"] = "1.00"
cte_os["icms_situacao_tributaria"] = "00"
cte_os["icms_valor"] = "0.17"
cte_os["indicador_inscricao_estadual_tomador"] = "9"
cte_os["inscricao_estadual_emitente"] = "12345678"
cte_os["logradouro_emitente"] = "Aeroporto Internacional de Salvador"
cte_os["logradouro_tomador"] = "Rua Jo\u00e3o"
cte_os["modal"] = "02"
cte_os["municipio_emitente"] = "Salvador"
cte_os["municipio_envio"] = "Abadia de Goi\u00e1s"
cte_os["municipio_fim"] = "Abadia dos Dourados"
cte_os["municipio_inicio"] = "Abadia de Goi\u00e1s"
cte_os["municipio_tomador"] = "Curitiba"
cte_os["natureza_operacao"] = "PREST. DE SERV. TRANSPORTE A ESTAB. COMERCIAL"
cte_os["nome_emitente"] = "ACME LTDA"
cte_os["nome_fantasia_emitente"] = "ACME"
cte_os["nome_fantasia_tomador"] = "Nome do tomador do servico aqui"
cte_os["nome_tomador"] = "NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL"
cte_os["numero_emitente"] = "S/N"
cte_os["numero_fatura"] = "1"
cte_os["numero_tomador"] = "1"
cte_os["pais_tomador"] = "BRASIL"
cte_os["quantidade"] = "1.00"
seguros_carga["nome_seguradora"] = "Nome da seguradora aqui"
seguros_carga["numero_apolice"] = "12345"
seguros_carga["responsavel_seguro"] = "4"
cte_os["telefone_emitente"] = "4133336666"
cte_os["tipo_documento"] = "0"
cte_os["tipo_servico"] = "6"
cte_os["uf_emitente"] = "BA"
cte_os["uf_envio"] = "GO"
cte_os["uf_fim"] = "MG"
cte_os["uf_inicio"] = "GO"
cte_os["uf_tomador"] = "PR"
cte_os["valor_desconto_fatura"] = "0.00"
cte_os["valor_inss"] = "0.10"
cte_os["valor_liquido_fatura"] = "1.00"
cte_os["valor_original_fatura"] = "1.00"
cte_os["valor_receber"] = "1.00"
cte_os["valor_total"] = "1.00"
cte_os["valor_total_tributos"] = "0.00"

# Adicionamos os dados das variaveis seguros_carga e documentos_referenciados como listas ao dicionario principal.
cte_os["seguros_carga"] = [seguros_carga]
cte_os["documentos_referenciados"] = [documentos_referenciados]

r = requests.post(url, params=ref, data=json.dumps(cte_os), auth=(token,""))

# Mostra na tela o codigo HTTP da requisicao e a mensagem de retorno da API.
print(r.status_code, r.text)