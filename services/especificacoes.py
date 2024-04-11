
import pandas as pd


def especificacao_1():
    propriedades = 'dados/propriedades.json'
    df = pd.read_json(propriedades)
    df = pd.json_normalize(df['propriedade'])
    df['identificador'] = (df['cd_oficial'].astype(str) + df['nr_unidade_exploracao'].astype(str)).astype(int)

    df.to_csv('propriedades_tratadas.csv')
    return df


def especificacao_2():
    dados_propriedade = 'dados/dados_propriedade.json'
    dados_propriedade = pd.read_json(dados_propriedade)
    dados_propriedade = pd.json_normalize(dados_propriedade['dados_propriedade'])
    propriedade = especificacao_1()
    print('df propriedade -->')
    print(propriedade)
    print('df dados propriedade -->')
    print(dados_propriedade)
    
    print('df tabelas concatenadas -->')
    df = pd.merge(propriedade, dados_propriedade, left_on='identificador', right_on='cd_propriedade', how= 'outer')
    
    df = df.fillna(0)
    df = df.replace([float('inf'), float('-inf')], 0)
    df['identificador'] = df['identificador'].astype(int)
    df['cd_propriedade'] = df['cd_propriedade'].astype(int)
    df['cd_especie'] = df['cd_especie'].astype(int)
    df['qt_animais'] = df['qt_animais'].astype(int)
    df['cd_oficial'] = df['cd_oficial'].astype(int)
    df['nr_unidade_exploracao'] = df['nr_unidade_exploracao'].astype(int)
    df['id_propriedade'] = df['id_propriedade'].astype(int)

    print(df)
    df.to_csv('especificacao2.csv')

    return df


def especificacao_3():
    propriedades = especificacao_1()
    df_propriedades = propriedades[['id_propriedade', 'identificador','nm_propriedade']].copy()

    risco_propriedade = 'dados/risco_propriedade.json'
    df_risco_propriedade = pd.read_json(risco_propriedade)
    df_risco_propriedade = pd.json_normalize(df_risco_propriedade['risco_propriedade'])
    
    df_remove = df_risco_propriedade.loc[(df_risco_propriedade['score_criterio'] == 0)]
    df_risco_propriedade = df_risco_propriedade.drop(df_remove.index)
    
   
    riscos = df_risco_propriedade.groupby('cd_propriedade')['nm_criterio'].agg(lambda x: ';'.join(x)).reset_index()
    riscos = riscos.rename(columns={'nm_criterio': 'riscos'})

    score_criterio = df_risco_propriedade.groupby('cd_propriedade')['score_criterio'].sum().reset_index()
    min_score = score_criterio['score_criterio'].min()
    max_score = score_criterio['score_criterio'].max()

    score_criterio['score_normalizado'] = (score_criterio['score_criterio'] - min_score) / (max_score - min_score)
    
    
    df = pd.merge(riscos, df_propriedades, left_on='cd_propriedade', right_on='id_propriedade', how= 'outer')
    df = pd.merge(score_criterio, df, left_on='cd_propriedade', right_on='id_propriedade', how= 'outer')
    
    df_final = df.drop(['cd_propriedade_x', 'score_criterio', 'cd_propriedade_y',
        'id_propriedade'], axis=1)
    print(df_final)
    
    df_final.to_csv('tabela_final.csv')

