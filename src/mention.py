#!/usr/bin/env python

from utils.mention_util import party_search_terms, politician_search_terms, extract_mentions
from tqdm import tqdm
import pandas as pd



def main():
  # Import raw data
  df = pd.read_pickle('data/minutewise.pkl')
  df.dropna(inplace=True)

  # Extract party mentions from raw data
  rows = extract_mentions(df, party_search_terms)

  # Create and export the new DataFrame from the list of rows
  party_df = pd.DataFrame(rows, columns=['medium', 'id', 'title', 'minute', 'date', 'search_term', 'extracted_string'])
  party_df.to_pickle('data/party_mentions.pkl')

  # Extract politician mentions from raw data
  rows = extract_mentions(df, politician_search_terms)

  # Create and export the new DataFrame from the list of rows
  politician_df = pd.DataFrame(rows, columns=['medium', 'id', 'title', 'minute', 'date', 'search_term', 'extracted_string'])
  politician_df.to_pickle('data/politician_mentions.pkl')


if __name__ == "__main__":
    main()