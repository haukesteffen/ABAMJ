#!/usr/bin/env python

from src.utils.analyze_mentions_util import analyze_mentions_df, saveplot
import pandas as pd


def analyze_mentions():
  # Import mentions data
  print('\n\nImporting mentions data...')
  party_df = pd.read_pickle('data/party_mentions.pkl')
  politician_df = pd.read_pickle('data/politician_mentions.pkl')

  # Get pivoted, standardized and zeromean dataframes
  print('Analyzing mentions...')
  party_pivot_df, party_standardized_df, party_zeromean_df = analyze_mentions_df(party_df)
  politician_pivot_df, politician_standardized_df, politician_zeromean_df = analyze_mentions_df(politician_df)

  # Save pickled dataframes
  print('Exporting dataframes...')
  party_pivot_df.to_pickle('results/dataframes/mentions/party_pivot_df.pkl')
  party_standardized_df.to_pickle('results/dataframes/mentions/party_standardized_df.pkl')
  party_zeromean_df.to_pickle('results/dataframes/mentions/party_zeromean_df.pkl')
  politician_pivot_df.to_pickle('results/dataframes/mentions/politician_pivot_df.pkl')
  politician_standardized_df.to_pickle('results/dataframes/mentions/politician_standardized_df.pkl')
  politician_zeromean_df.to_pickle('results/dataframes/mentions/politician_zeromean_df.pkl')

  # Save plots
  print('Exporting plots...')
  saveplot(party_standardized_df, 
           'Party Mentions', 
           'results/plots/mentions/party_mentions.pdf')
  saveplot(party_zeromean_df, 
           'Party Mentions (zero mean)', 
           'results/plots/mentions/party_mentions_zeromean.pdf')
  saveplot(politician_standardized_df, 
           'Politician Mentions', 
           'results/plots/mentions/politician_mentions.pdf')
  saveplot(politician_zeromean_df, 
           'Politician Mentions (zero mean)', 
           'results/plots/mentions/politician_mentions_zeromean.pdf')


if __name__ == "__main__":
    analyze_mentions()
