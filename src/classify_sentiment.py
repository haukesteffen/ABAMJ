#!/usr/bin/env python

from src.utils.classify_sentiment_util import extract_sentiment_df
import pandas as pd


def classify_sentiment():
  # Import mention data
  party_df = pd.read_pickle('data/party_mentions.pkl')
  politician_df = pd.read_pickle('data/politician_mentions.pkl')

  # Classify sentiment of party mentions and save pickled dataframe
  print('\n\nClassifying sentiment of party mentions...')
  sentiment_classified_party_df = extract_sentiment_df(party_df)
  sentiment_classified_party_df.to_pickle('data/party_sentiment_classifications.pkl')

  # Classify sentiment of politician mentions and save pickled dataframe
  print('Classifying sentiment of politician mentions...')
  sentiment_classified_politician_df = extract_sentiment_df(politician_df)
  sentiment_classified_politician_df.to_pickle('data/politician_sentiment_classifications.pkl')


if __name__ == "__main__":
    classify_sentiment()
