# -*- coding: utf-8 -*-

import os, csv
import pandas as pd


def sortFreq(path):
    df = pd.read_csv(path + '/' + 'database.csv')
    df_count = df.groupby(['POS-Tags']).sum().reset_index()
    df_final_1 = df_count[['POS-Tags', 'Occurrences']]

    df_people_num = df.groupby(['POS-Tags']).count().reset_index()
    df_people_num['Occurrences'] = df_people_num['Occurrences'].apply(lambda x: x // 5)
    df_final_2 = df_people_num[['POS-Tags', 'Occurrences']]

    df_final_3 = pd.merge(df_final_1, df_final_2, on='POS-Tags')
    df_final = pd.merge(df_final_3, df, on='POS-Tags')
    df_final = df_final[['POS-Tags', 'Occurrences_x', 'Occurrences', 'Bigram']]
    df_final = df_final.sort_values(['Occurrences_x', 'Occurrences'], ascending=False)
    df_final.to_csv(path + '/' + 'pos_freq.csv', index=False)

    d_new = df_final[['POS-Tags', 'Occurrences_x']]
    d_new = d_new.drop_duplicates()

    d_lists = {col: d_new[col].tolist() for col in d_new.columns}
    l_pos = d_lists.get('POS-Tags')
    l_occ = d_lists.get('Occurrences_x')

    pos_freq_dict = dict(zip(l_pos, l_occ))
    return pos_freq_dict
