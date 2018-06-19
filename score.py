#!/usr/bin/env python
# -*- coding: windows-1252 -*-

def gerarScore(df,grupo):

    import pandas as pd
    import csv
    import sys
    import statistics
    import numpy as np
    total = []

    with open('worldcup2018.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            pais = row[0]
            if row[1] != grupo:
                continue

            timeEmcasa = df[df['home_team'] == pais ]

            scorePro = timeEmcasa[timeEmcasa['home_score'] !=0]
            scoreAgainst = timeEmcasa[timeEmcasa['away_score'] !=0]


            timeForaCasa = df[df['away_team'] == pais ]
            time = pd.concat([timeEmcasa,timeForaCasa])
            scorePro2 = timeForaCasa[timeForaCasa['away_score'] !=0]
            scoreAgainst2 = timeForaCasa[timeForaCasa['home_score'] !=0]


            totalPartidas = len(time)
            vitorias = time[time['winner'] == 1 ]
            derrotas = time[time['loser']  == 1 ]
            empates = time[time['winner'] == 3 ]


            #print(len(vitorias.winner.values))
            #print(totalPartidas)

            porcentagemVitorias = float(len(vitorias.winner.values))/ totalPartidas
            aproveitamento = porcentagemVitorias * 100
            score = time[time['away_score'] != 0]
            scoreEmCasa = time[time['home_score'] != 0]


            sumScore = []
            sumScore = np.append(scorePro.home_score.values,scorePro2.away_score.values)

            sumScoreAgainst = []
            sumScoreAgainst = np.append(scoreAgainst.away_score.values, scoreAgainst2.home_score.values)

            total.append([grupo,pais,len(vitorias.winner.values),len(derrotas.loser.values), len(empates.winner.values),totalPartidas,statistics.variance(sumScore),statistics.variance(sumScoreAgainst),aproveitamento])




    return total
