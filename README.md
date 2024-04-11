
# Descrição dos arquivos:

Arquivo **propriedade.json**: Lista as propriedades onde são criados os animais.
- **id_propriedade**: Identificador único;
- **cd_oficial**: Código oficial da propriedade;
- **nr_unidade_exploracao**: Número da unidade de exploração da propriedade;
- **nm_propriedade**: Nome da propriedade;  
- **dt_fim**: Se preenchida, mostra a data em que a propriedade foi inativada.

Arquivo **dados_propriedade.json**: Lista as espécies de animais cadastradas para cada Unidade de exploração (UEP). 
- **cd_propriedade**: Identificador único, sendo a concatenação dos campos 'cd_oficial' e 'nr_unidade_exploracao' do arquivo “propriedade”;
- **cd_especie**: Espécie criada na unidade de exploração;
- **qt_animais**: Quantidade de animais presentes na unidade de exploração.	

Arquivo **risco_propriedade.json**: Lista as propriedades e os riscos de doenças animais associados a elas. 
- **id_risco_propriedade**: Identificador único, um sequencial comum;
- **cd_propriedade**: Referência a coluna 'id_propriedade' do arquivo 'propriedade' - nessa coluna não ocorre a concatenação dos campos cd_oficial e nr_unidade_exploracao;
- **nm_criterio**: String para descrever o critério de risco em que a propriedade se enquadra;
- **score_criterio**: Pontuação do critério.



**Especificação 1**. Carregar o arquivo “propriedades.json” através dos endpoints disponibilizados via e-mail. Após extração, criar um campo chamado 'identificador' através da concatenação dos campos 'cd_oficial' e 'nr_unidade_exploracao'.

**Especificação 2**. Carregar o arquivo “dados_propriedade.json” através dos endpoints disponibilizados via e-mail. Após extração e criação do campo “identificador” (cd_oficial + nr_unidade_exploracao), realizar a junção das tabelas “propriedades” e “dados_propriedade”. 

propriedade[identificador] == dados_propriedade[cd_propriedade]

**Especificação 3**. Carregar o arquivo 'risco_propriedade.json' e criar uma nova tabela contendo as seguintes colunas:
- **identificador**: Colunas 'cd_oficial' e 'nr_unidade_exploracao' do arquivo 'propriedade' concatenadas;
- **nm_propriedade**: Coluna 'nm_propriedade' do arquivo 'propriedade'; 
- **riscos**: Junção de todos os 'nm_criterio' associados a propriedade em questão. Eles devem ser separados por ponto e vírgula e deve ser um texto normal. Exemplo: "Propriedade próxima de aterros sanitários; Fronteira com Argentina";
- **score_normalizado**: Pontuação da propriedade com os dados normalizados referentes a coluna “score_criterio” do arquivo 'risco_propriedade'.

