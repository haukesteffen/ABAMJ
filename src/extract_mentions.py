#!/usr/bin/env python

from utils.extract_mentions_util import party_search_terms, politician_search_terms, extract_mentions
from tqdm import tqdm
import pandas as pd
from pandarallel import pandarallel



def main():
  # Import raw data
  df = pd.concat([
    pd.read_pickle('data/minutewise.pkl').dropna(),
    pd.read_pickle('data/mediathek_data.pkl')
  ], axis = 0
  )

  # Initialize pandarallel
  pandarallel.initialize(progress_bar=True)

  # Extract party mentions from raw data
  party_dict = df.parallel_apply(extract_mentions, search_terms=party_search_terms, axis=1)

  # Create and export the new DataFrame from the list of rows
  party_df = pd.DataFrame(party_dict.dropna().explode().to_list())
  party_df.to_pickle('data/party_mentions.pkl')

  # Extract politician mentions from raw data
  politician_dict = df.parallel_apply(extract_mentions, search_terms=politician_search_terms, axis=1)

  # Create and export the new DataFrame from the list of rows
  politician_df = pd.DataFrame(politician_dict.dropna().explode().to_list())
  politician_df.to_pickle('data/politician_mentions.pkl')


if __name__ == "__main__":
    main()