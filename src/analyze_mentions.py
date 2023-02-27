#!/usr/bin/env python

from utils.analyze_mentions_util import analyze_mentions, saveplot
import pandas as pd



def main():
  # Import raw data
  party_df = pd.read_pickle('data/party_mentions.pkl')
  politician_df = pd.read_pickle('data/politician_mentions.pkl')

  # Get pivoted dataframes and zeromean dataframes
  party_pivot_df, party_standardized_df, party_zeromean_df = analyze_mentions(party_df)
  politician_pivot_df, politician_standardized_df, politician_zeromean_df = analyze_mentions(politician_df)

  # Save pickled dataframes
  party_pivot_df.to_pickle('results/dataframes/party_pivot_df.pkl')
  party_standardized_df.to_pickle('results/dataframes/party_standardized_df.pkl')
  party_zeromean_df.to_pickle('results/dataframes/party_zeromean_df.pkl')
  politician_pivot_df.to_pickle('results/dataframes/politician_pivot_df.pkl')
  politician_standardized_df.to_pickle('results/dataframes/politician_standardized_df.pkl')
  politician_zeromean_df.to_pickle('results/dataframes/politician_zeromean_df.pkl')

  # Save plots
  saveplot(party_standardized_df, 'Party Mentions', 'results/plots/party_mentions.pdf')
  saveplot(party_zeromean_df, 'Party Mentions (zero mean)', 'results/plots/party_mentions_zeromean.pdf')
  saveplot(politician_standardized_df, 'Politician Mentions', 'results/plots/politician_mentions.pdf')
  saveplot(politician_zeromean_df, 'Politician Mentions (zero mean)', 'results/plots/politician_mentions_zeromean.pdf')


if __name__ == "__main__":
    main()