#!/usr/bin/env python
# -*- coding: windows-1252 -*-

import pandas as pd
import csv
import sys
import statistics


df = pd.read_csv('results.csv') #partidas internacionais desde 1800
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




dfResultados



grupo = sys.argv[1]
print("Grupo")
print (grupo)
dict = []
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

        vitorias = time[time['winner'] == 1 ]
        derrotas = time[time['loser']  == 1 ]
        empates = time[time['winner'] == 3 ]



        print("vitorias")
        print(sum(vitorias.winner.values))

        print("derrotas")
        print(sum(derrotas.loser.values))

        print("empates")
        print(sum(empates.winner.values))

        if pais == 'Russia':
            print("Gols em casa")
            #print(time.home_score.values)
            score = time[time['home_score'] != 0]
            print(statistics.median(score.home_score.values))
            print(statistics.variance(score.home_score.values))

        else:
            print("Gols fora de casa")
            #print(time.away_score.values)
            score = time[time['away_score'] != 0]
            print(statistics.median(score.away_score.values))
            print(statistics.variance(score.away_score.values))
        print("\n")
        print("--------------------------")
