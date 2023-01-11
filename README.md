# Análise Orçamentária 2022

## Análise da Execução Orçamentária do 11° Batalhão de Polícia do Exército no ano de 2022

## 1. Sumário

* Contexto
* Dados
* Análise
* Conclusão

## 2. Contexto

O controle da execução orçamentária na administração pública brasileira é de extrema importância.
Diferente da administração privada, a administração pública deve seguir regras mais rigidas, conforme disposto nas leis e demais normas legais. Tais normas destacam a importância da transparência, da economicidade e da eficiência. Esse cenário apresenta desafios para os administradores públicos, que devem respeitar as limitações e buscar atender as necessidades de sua repartição.

Nesse contexto, existem alguns documentos e definições importantes para a compreensão da presente análise:

* Crédito - Representado pela Nota de Crédito (NC), representa a disponibilidade de recursos do orçamento público para o empenho e futuro pagamento;
* Empenho - Executado por meio da Nota de Empenho (NE), representa o compromisso da Adm. Pública em realizar o pagamento uma vez que o material ou serviço contratado com o fornecedor seja entregue conforme as especificações;
* Liquidação - Executada por meio de uma Nota de Sistema (NS), é o ato que atesta o recebimento do bem empenhado e libera o valor para realização do pagamento;
* Pagamento - Executado através de uma Ordem Bancária (OB), é a última fase da despesa, realizando a efetiva transferência do valor monetário para o fornecedor.

## 3. Dados

Os dados foram extraídos utilizando as APIs disponibilizada no [Portal da Transparência](https://api.portaldatransparencia.gov.br/swagger-ui.html) para consulta de documentos da despesa pública. O único dado externo utilizado foi uma lista com os empenhos realizados por esta Organização Militar.
As APIs utilizadas para a extração necessitam de um cadastro no site do Portal da Transparência, que gera um token que foi utilizado no código, com o objetivo de limitar a utilização.

```Python
for emp in ne_160_list:
    data = requests.get(
    f'https://api.portaldatransparencia.gov.br/api-de-dados/despesas/documentos/16029700001{emp}',
    headers={"chave-api-dados":token}
    )
    data_df = data.json()
    data_df = pd.json_normalize(data_df)
    ne_160_df = pd.concat([ne_160_df,data_df])
```
Essa API extrais os dados de uma base de dados que é atualizada diariamente, então existe um atraso de 24h para que novas informações sejam adicionadas.
Friso que todas as informações apresentadas nesse projeto são abertas ao público e disponibilizadas pelo Governo Federal, conforme as leis de acesso à informação. O único dado externo ao Portal utilizado foi a lista de empenhos que procuramos.

## 4. Análise

Os gráficos e visualizações utilizadas nesse relatório estão disponíveis no Dashboard disponibilizado [aqui](https://github.com/lucas-a-correa/Analise-Orcamentaria-2022/blob/main/An%C3%A1lise%20Or%C3%A7ament%C3%A1ria.pbix), e pode ser acompanhado interativamente em conjunto.
