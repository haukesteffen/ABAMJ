#!/usr/bin/env python

from utils.classify_sentiment_util import extract_sentiment_df
import pandas as pd



def main():
  party_df = pd.read_pickle('data/party_mentions.pkl')
  politician_df = pd.read_pickle('data/politician_mentions.pkl')

  sentiment_classified_party_df = extract_sentiment_df(party_df)
  sentiment_classified_party_df.to_pickle('data/party_sentiment_classifications.pkl')

  sentiment_classified_politician_df = extract_sentiment_df(politician_df)
  sentiment_classified_politician_df.to_pickle('data/politician_sentiment_classifications.pkl')



if __name__ == "__main__":
    main()