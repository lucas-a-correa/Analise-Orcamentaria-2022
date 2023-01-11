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

#### Crédito Recebido e Empenhado

![Image](/Charts/Recursos_Recebidos_Primária_Geral.PNG)

O gráfico ilustra que o 11° BPE recebeu um montante superior a R$644 mil, tendo a maior proporção desses recursos (76.75%) sido descentralizada pelo Comando Logístico (COLOG), seguido pelo Diretoria de Gestão Orçamentária (DGO) (15.51%), o Comando de Operações Terrestres (COTER) (7.53%) e uma proporção insignificante pelo Departamento de Educação e Cultura (DECEx) (0.21%). O valor empenhado representa aquele que foi efetivamente comprometido, representando 94.76% dos recursos recebidos. O valor remanescente é constituído tanto por valores residuais (montantes reduzidos que permanecem nas notas de crédito após a execução dos empenhos e que são recolhidos para redistribuição) quanto por valores que foram recolhidos devido a descumprimento de prazos ou erros na descentralização. Esse montante foi executado em 94 empenhos, tendo média de quase R$6,500.00 por empenho.

![Image](/Charts/Recursos_Recebidos_Det_Primária.PNG)

O montante de recursos financeiros referentes ao COLOG atingiu a cifra de R$ 455,41 mil, distribuídos por meio de 33 empenhos, com um valor médio de R$ 13,8 mil e um índice de empenho de 92,05%. Estes créditos são destinados para suprir as necessidades de aquisição de uniformes e equipamentos para a tropa, peças e manutenção dos veículos, além da alimentação e medicamentos para os animais empregados pelo Batalhão. O 11° BPE é uma unidade com características distintas em relação às Organizações Militares tradicionais do exército, realizando tarefas de policiamento e controle de trânsito na Vila Militar - RJ, além de possuir uma seção especializada em cães de guerra para apoio em operações de busca por drogas, explosivos e armamentos. Essas atividades específicas justificam a proporção dos recursos financeiros que são recebidos.

Os recursos orçamentários relacionadas à DGO apresentam um montante total de R$ 97,51 mil, sendo distribuídas por meio de 47 empenhos, com uma média de R$ 2,07 mil por empenho, e um índice de comprometimento de 97,51%. A DGO é responsável por suprir as necessidades relacionadas aos aspectos vegetativos da Organização Militar, como materiais de uso administrativo, itens de limpeza e serviços de manutenção de equipamentos. O 11° BPE, atualmente, conta com um contingente de aproximadamente 500 militares, o que requer um elevado grau de planejamento para garantir que os recursos financeiros sejam destinados de forma adequada a atender às necessidades do Batalhão.

Os créditos empenhados com o valor recebido pelo COTER são de um total de R$ 21,64 mil, em 12 empenhos, com uma média de R$ 1,8 mil, e um percentual de 44,57%. É importante investigar as causas que levaram a esse baixo percentual de empenho, seja devido a problemas na execução de prazos pelo setor administrativo ou devido a ajustes necessários nas distribuições financeiras.
O COTER é responsável por atender às necessidades de preparo e emprego da tropa, incluindo a manutenção das instalações utilizadas na formação anual de novos soldados, materiais de instrução e equipamentos empregados em missões. Como uma unidade altamente operacional e com operações diárias, é vital realizar uma análise sobre a adequação dos recursos financeiros às necessidades do Batalhão e como isso impacta na execução das missões.

Finalmente, a Dotação Financeira recebido do DECEx foi aplicada em apenas um empenho, com o valor de R$ 1,29 mil. O DECEx é o órgão responsável por suprir as necessidades educacionais e culturais do Exército. Como o 11° BPE não é uma instituição de ensino é pouco comum o recebimento de dotações financeiras deste órgão.Dessa forma, é provável que se trate de crédito eventual, sido recebido por um motivo pontual.

#### Liquidação e Pagamento

A liquidação, como foi mencionado anteriormente, é o formal reconhecimento no sistema que o bem adquirido foi recebido e está em condições adequadas para que o pagamento seja realizado. É comum que o prazo para o recebimento e liquidação seja de 30 dias, com exceção para casos específicos, tais como obras ou serviços que requeiram um período de tempo superior. Além disso, a meta estabelecida para o pagamento após a liquidação também é de 30 dias. É importante ressaltar que a meta estabelecida anualmente para a execução é de 80%, com o objetivo de evitar inscrição de despesas em Restos a Pagar para o exercício seguinte.

![Image](/Charts/Liq_Pag_Primária_Geral.PNG)

É evidente que os índices alcançados foram satisfatórios, pois tivemos um alcance acima da meta estabelecida, com 87,75% de liquidação e 86,04% de pagamento.  No entanto, é preciso mencionar que o prazo para a liquidação foi significativamente inferior ao esperado, com uma média de 82 dias e um máximo alarmante de 222 dias. Isso sugere que precisamos redobrar os esforços para melhorar a fiscalização e a gestão, a fim de evitar atrasos que possam gerar desnecessários encargos para a União. No pagamento observamos uma média acima do esperado, com 17 dias para a liquidação, e um máximo de 40 dias, apenas 10 dias além do limite,  o que é indicativo de um controle financeiro satisfatório.

![image](/Charts/Liq_Pag_Det_Primária.PNG)

Nas demonstrações por UGR vemos o mesmo padrão, com alcance das metas de porcentagem, atrasos significativos na liquidação e pagamentos dentro do prazo estipulado. A única exceção é o crédito recebido pelo DECEx, que não foi liquidado em 2022, e por se tratar de apenas um empenho, apresentando com uma porcentagem de 0%.

#### Fluxo de Recursos

![image](/Charts/Fluxo_Desp_Primária.PNG)

Analisando os dados financeiros ao longo do ano, podemos observar a presença de dois picos de recebimento de créditos, no início e no final do ano. Essa distribuição tem relação com a rotina de aquisições na Administração Pública. Os créditos são distribuídos no início do ano para que haja tempo hábil para os processos de licitação, aquisição, liquidação e pagamento. No final do ano, é comum haver redistribuição de créditos não utilizados, de acordo com as necessidades da Força. É importante mencionar que durante o ano são distribuídos créditos de menor valor, normalmente destinados à "vida vegetativa" da organização militar.
Na análise dos empenhos, liquidações e pagamentos, notamos uma maior concentração no final do ano. Isso se deve, em parte, ao tempo necessário para os processos administrativos, como mencionado anteriormente, mas também pode ser sinal de falta de planejamento. Normalmente, os créditos recebidos por uma organização militar são semelhantes ao longo dos anos, exceto em situações específicas, como a pandemia de COVID-19 em 2020 ou a Intervenção Federal no Rio de Janeiro em 2018. Isso permite o planejamento das despesas, com o início dos processos de lciitação no ano anterior ao efetivo recebimento do crédito. Como ainda assim vemos uma concentração no final do ano, podemos inferir que não está sendo realizado um planejamento efetivo, atrasando os empenho e, por consequência, as liquidações e pagamentos.

### Fonte Secundária

![image](/Charts/Recursos_Recebidos_Secundária_Geral.PNG)

Este gráfico nos mostra os créditos recebidos na fonte secundária. O Departamento-Geral do Pessoal (DGP) corresponde a 70,35% do valor,e é referente ao crédito destinado ao atendimento de saúde e odontológico, dos militares e seus dependentes. Já o crédito descentralizado pelo Fundo do Exército (FEX) é gerado pela própria OM, com cessões de uso e Próprio Nacional (Moradia dos Militares). Por se tratar de um crédito de geração prórpria e utilizado para fins específicos, possui um valor inferios, totalizando R$ 111,28 Mil, com R$ 109,19 mil (98,12%) empenhados, em 42 empenhos, com uma média de R$ 2,6 mil.

#### Crédito Recebido e Empenhado

![image](/Charts/Recursos_Recebidos_Det_Secundária.PNG)

A descentralização do DGP totaliza R$ 78,28 mil, com 33 empenhos totalizando R$ 78,25 mil (99,96%) e uma média de R$ 2,37 Mil.
Esse crédito visa atender a Seção de Saúde do Batalhão, com a aquisição de medicamentos e equipamentos, para viabilizar o atendimento médico e odontológico dos militares e seus dependentes.

O crédito recebido pelo FEX totaliza R$ 33 mil, com 9 empenhos com um valor de R$ 30,93 mil (93,76%) e média de R$ 3,44 mil.
Este crédito atende necessidades pontuais da OM, sendo solicitada juntamente com a fundamentação do pedido. Normalmente são utilizados para a manutenção das moradias dos militares ou das instalações da Unidade, bem como para o atendimento de necessidades que não conseguiram ser atendidas pelo crédito primário recebido.

#### Liquidação e Pagamento

![image](/Charts/Liq_Pag_Secundária_Geral.PNG)

Na demonstração das liquidações e pagamentos encontramos uma situação parecida com a fonte primária. As metas foram atingidas, com 85,78% de liquidação e 83,18% de pagamento, com altos atrasos na liquidação (Média de 68 dias) e pagamentos dentro do prazo, situação que é refletida nos créditos detalhados das UGR.

![image](/Charts/Liq_Pag_Det_Secundária.PNG)

#### Fluxo de Recursos

![image](/Charts/Fluxo_Desp_Secundária.PNG)

Analisando os dados de créditos recebidos por meio de fontes secundárias, notamos um padrão distinto em comparação com as fontes primárias. O pico de recebimento de créditos ocorre no início do ano, bem como o de empenhos.  Isso sugere um planejamento mais eficiente das aquisições realizado pelos setores responsáveis. As liquidações e pagamentos acontecem durante o ano, o que é esperado pelos prazos e ciclo empenho-recebimento-pagamento das fases da despesa.

## 5. Conclusão

