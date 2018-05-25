#!/usr/bin/env python
# -*- coding: windows-1252 -*-

import pandas as pd
import csv
import sys



def estatisticasTime(time,pais):
    import numpy as np
    vitorias = time[time['winner'] == pais].count()
    derrotas = time[time['winner'] != pais].count()
    partidas = time.date.count()
    golsEmcasa = time.home_score.sum()
    golsForaDeCasa = time.away_score.sum()
    totalGolsPorPartida =  golsForaDeCasa + golsEmcasa
    mediaGols = totalGolsPorPartida / partidas
    aproveitamento = 100 * float (vitorias.date ) /float (partidas)
    estatisticas = {"partidas":partidas,"aproveitamento":round(aproveitamento,3), "time":pais,"gols": mediaGols, "vitorias":vitorias.date,"derrotas":derrotas.date}

    return estatisticas;


df = pd.read_csv('results.csv') #partidas internacionais desde 1800
dfwc = pd.read_csv('worldcup2018.csv') 


#verifica vencedor
def winner(row):
    if row['home_score'] > row['away_score']: return row['home_team']
    elif row['home_score'] < row['away_score']: return row['away_team']
    else: return 'DRAW'

df['winner'] = df.apply(lambda row: winner(row), axis=1)


#verifica perdedor
def loser(row):
    if row['home_score'] < row['away_score']: return row['home_team']
    elif row['home_score'] > row['away_score']: return row['away_team']
    else: return 'DRAW'

df['loser'] = df.apply(lambda row: loser(row), axis=1)


grupo = sys.argv[1]
print("Grupo")
print (grupo)
with open('worldcup2018.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        pais = row[0]
        if row[1] != grupo:
            continue
        print(pais)
        timeEmcasa = df[df['home_team'] == pais ]
        timeForaCasa = df[df['away_team'] == pais ]
        time = pd.concat([timeEmcasa,timeForaCasa])
        if time.date.count() == 0:
            continue;
        print(estatisticasTime(time,pais))
