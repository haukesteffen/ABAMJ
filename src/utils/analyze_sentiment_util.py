import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


media = [
    'NachDenkSeiten', 
    'taz', 
    'DER SPIEGEL', 
    'ARD', 
    'ZDF', 
    'Bayerischer Rundfunk', 
    'ntv Nachrichten', 
    'faz', 
    'WELT', 
    'BILD', 
    'COMPACTTV']
parties = [
    'linke',
    'grüne',
    'spd',
    'fdp',
    'cdu',
    'csu',
    'afd']


def analyze_sentiment_df(input_df, mention_df):
    pivot_df = pd.pivot_table(
        input_df, 
        index='medium', 
        columns='party', 
        values='title', 
        aggfunc='count', 
        fill_value=0).reindex(media)[parties]
    
    standardized_df = pivot_df.div(mention_df)

    zeromean_df = standardized_df - standardized_df.mean()

    return pivot_df, standardized_df, zeromean_df


def saveplot(df, title, path):
    width = 6.2
    height = width*11/21

    plt.rcParams['axes.unicode_minus'] = False
    plt.rc('axes', titlesize=12)
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)


    f, ax = plt.subplots(figsize=(9, 8))
    f.set_size_inches(width, height)
    f.subplots_adjust(left=0.13, bottom=.16, right=.99, top=.91)
    
    df_to_plot = df.copy()
    sns.heatmap(
        df_to_plot, 
        annot=True, 
        linewidths=.5, 
        ax=ax, 
        fmt=".1%", 
        center=np.nanmean(df_to_plot), 
        cbar=False, 
        cmap=sns.diverging_palette(145, 20, as_cmap=True).reversed())

    ax.set_xlabel('Party', fontsize=12, color='black')
    ax.set_ylabel('Medium', fontsize=12, color='black')
    ax.set_title(title, fontsize=12, color='black')
    ax.set_xticklabels(
        ['Linke', 'Grüne', 'SPD', 'FDP', 'CDU', 'CSU', 'AfD'], 
        size=12, 
        color='black')
    ax.set_yticklabels(
        ['NDS', 'taz', 'Sp', 'ARD', 'ZDF', 'BR', 'ntv', 'faz', 'WELT', 'BILD', 'CTV'], 
        size=12, 
        color='black')
    
    f.savefig(path)
    return
