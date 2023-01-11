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

As organizações militares recebem créditos de duas fontes principais: A Fonte Primária, representada pelo código iniciado por '160', que é composta por recursos descentralizados pelo orçamento do governo federal, conforme a Lei Orçamentária Anual, e a Fonte Secundária, cujo código inicia com '167', composta por recursos gerados pelo próprio Exército, como por contratos de cessão de uso, valores pagos por moradores de Próprio Residencial Nacional e valores pagos pelos usuários do sistema de saúde do Exército. Os recursos dessas duas fontes possuem finalidades diferentes e, por isso, serão analisados separadamente.

### Fonte Primária



Conforme o gráfico acima, observamos que o 11° BPE recebeu no total mais de R$ 644 mil, com a grande maioria sendo descentralizada pelo Comando Logístico (COLOG) (76,75%), seguido pela Diretoria de Gestão Orçamentária (DGO) (15,51%), pelo Comando de Operações Terrestres (COER) (7,53%) e uma pequena parte do Departamento de Educação e Cultura (DECEx) (0,21%). O total empenhado representa o recurso que efetivamente foi empenhado, compondo 94,76% dos valores recebidos. O valor restante é composto tanto por valores residuais (pequenos valores que restam nas notas de crédito após a execução dos empenhos e que são recolhidos para redistribuição) quanto por valores recolhidos por não cumprimento de prazos ou por erros na descentralização. Esse valor foi executado em 94 empenhos, resultando em uma média de quase R$ 6.500,00 por empenho.



Os empenhos com os créditos recebidos pelo COLOG somam um total de R$ 455,41 mil, distribuídos em 33 empenhos, com uma média de R$ 13,8 mil, e um percentual de empenho de 92,05%.
Os créditos distribuídos pelo COLOG são destinados para a aquisição de uniformes e equipamentos da tropa, peças e manutenção de veículos e alimentação e medicamentos para os animais da Organização Militar. O 11° BPE é um batalhão com uma realidade diferente de OMs ordinárias do exército, realizando o policiamento e o controle de trânsito da Vila Militar - RJ, bem como possuindo uma Seção de Cães de Guerra para apoio no policiamento e missões de farejamento de drogas, bombas e armamento. Todas essas missões exigem equipamento diferenciado, bem como a manutenção constante dos animais e viaturas, o que explica a proporção dos créditos recebidos.



Os empenhos referentes à DGO somam R$ 97,51 mil, em 47 empenhos, e uma média de R$ 2,07 mil por empenho, atingindo um percentual de 97,51% de empenho. 
A DGO atende as necessidades vegetativas da OM, como materiais de uso administrativo e materiais para limpeza, bem como serviços de manutenção de aparelhos da Unidade. O 11° BPE, atualmente, é composto por um efetivo de cerca de 500 militares, o que exige um alto nível de planejamento para que esse crédito atenda todas as necessidades do Batalhão.



Os créditos empenhados com o valor recebido pelo COTER são de um total de R$ 21,64 mil, em 12 empenhos, com uma média de R$ 1,8 mil, e um percentual de 44,57%. É importante verificar quais os motivos para um percentual de empenho tão baixo, se houve problemas no cumprimento de prazos pela equipe administrativa, ou se são referentes a recolhimentos por erro nas distribuições.
O COTER atende às necessidades de preparo e emprego da tropa. Isso engloba a manutenção de instalações para a formação anual de novos soldados, materiais utilizados nas instruções e equipamentos empregados em missões. Como um Batalhão altamente operacional e que é empregado diariamente é importante realizar um levantamento do atendimento das necessidades pelo crédito recebido e como isso está afetando o efetivo cumprimento de missões.



Por fim, o crédito recebido pelo DECEx foi empregado em apenas um empenho, no valor de R$ 1,29 mil. O DECEx é responsável pelo atendimento de necessidades de ensino e culturais do Exército
