#!/usr/bin/env python

from utils.analyze_sentiment_util import analyze_sentiment, saveplot
import pandas as pd


def main():
  # Import sentiment and mentions data
  party_sentiment_df = pd.read_pickle('data/party_sentiment_classifications.pkl')
  party_mentions_df = pd.read_pickle('results/dataframes/mentions/party_pivot_df.pkl')

  # Split sentiment dataframes by positive, neutral and negative sentiments
  party_positive_classifications = party_sentiment_df[party_sentiment_df['positive']]
  party_neutral_classifications = party_sentiment_df[party_sentiment_df['neutral']]
  party_negative_classifications = party_sentiment_df[party_sentiment_df['negative']]

  # Get pivoted, standardized and zeromean sentiment dataframes for each sentiment
  party_positive_pivot, party_positive_standardized, party_positive_zeromean = analyze_sentiment(party_positive_classifications, party_mentions_df)
  party_neutral_pivot, party_neutral_standardized, party_neutral_zeromean = analyze_sentiment(party_neutral_classifications, party_mentions_df)
  party_negative_pivot, party_negative_standardized, party_negative_zeromean = analyze_sentiment(party_negative_classifications, party_mentions_df)

  # Save pickled dataframes
  party_positive_pivot.to_pickle('results/dataframes/sentiment/party_positive_pivot_df.pkl')
  party_positive_standardized.to_pickle('results/dataframes/sentiment/party_positive_standardized.pkl')
  party_positive_zeromean.to_pickle('results/dataframes/sentiment/party_positive_zeromean.pkl')

  party_neutral_pivot.to_pickle('results/dataframes/sentiment/party_neutral_pivot.pkl')
  party_neutral_standardized.to_pickle('results/dataframes/sentiment/party_neutral_standardized.pkl')
  party_neutral_zeromean.to_pickle('results/dataframes/sentiment/party_neutral_zeromean.pkl')

  party_negative_pivot.to_pickle('results/dataframes/sentiment/party_negative_pivot.pkl')
  party_negative_standardized.to_pickle('results/dataframes/sentiment/party_negative_standardized.pkl')
  party_negative_zeromean.to_pickle('results/dataframes/sentiment/party_negative_zeromean.pkl')

  # Save plots
  saveplot(party_positive_standardized, 
           'Positive Party Mentions', 
           'results/plots/sentiment/party_positive_standardized.pdf')
  saveplot(party_positive_zeromean, 
           'Positive Party Mentions (zero mean)', 
           'results/plots/sentiment/party_positive_zeromean.pdf')

  saveplot(party_neutral_standardized, 
           'Neutral Party Mentions', 
           'results/plots/sentiment/party_neutral_standardized.pdf')
  saveplot(party_neutral_zeromean, 
           'Neutral Party Mentions (zero mean)', 
           'results/plots/sentiment/party_neutral_zeromean.pdf')
  
  saveplot(party_negative_standardized, 
           'Negative Party Mentions', 
           'results/plots/sentiment/party_negative_standardized.pdf')
  saveplot(party_negative_zeromean, 
           'Negative Party Mentions (zero mean)', 
           'results/plots/sentiment/party_negative_zeromean.pdf')


if __name__ == "__main__":
    main()
