#!/usr/bin/env python
# -*- coding: windows-1252 -*-

import pandas as pd
import csv
import numpy as np
from score import gerarScore

diretorioRaiz =  "/var/www/python/worldcup/"


df = pd.read_csv('results.csv')
dfwc = pd.read_csv('worldcup2018.csv')


#verifica vencedor
def winner(row):
    if row['home_score'] > row['away_score']: return 1
    elif row['home_score'] < row['away_score']: return 0
    else: return 3

df['winner'] = df.apply(lambda row: winner(row), axis=1)



#verifica perdedor
def loser(row):
    if row['home_score'] < row['away_score']: return 1
    elif row['home_score'] > row['away_score']: return 0
    else: return 3

df['loser'] = df.apply(lambda row: loser(row), axis=1)



grupos = ['A',"B","C","D","E","F","G","H"]
totalScore = []
value = 0
for grupo in grupos:
    scorePorGrupo = gerarScore(df,grupo)
    for score in scorePorGrupo:
        #print(score)
        totalScore.append(score)
        value = value +1
        #print(type(score))


columns = ['Grupo','Selecao', 'Vitorias', 'Derrotas','Empates','Partidas','Score Pro','Score Contra',"Aproveitamento"]
dfTotal = pd.DataFrame(totalScore, columns=columns)

dfTotal = dfTotal.sort_values(["Grupo"])

dfTotal.to_csv(diretorioRaiz+'score.csv', index=False)
print('done')
#print(dfTotal[dfTotal['Selecao'] =='Brazil'])
#print(dfTotal[dfTotal['Selecao'] == 'Saudi Arabia'])
#print(dfTotalVitorias)
