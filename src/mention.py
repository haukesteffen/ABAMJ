from utils.mention_util import *
from tqdm import tqdm
import pandas as pd

# Import raw data
df = pd.read_pickle('data/data.pkl')
df.dropna(inplace=True)

# Create an empty list to store the rows of the new DataFrame
rows = []

# Iterate over the rows of the original DataFrame
for _, row in tqdm(df.iterrows(), total=df.shape[0]):
  medium = row['medium']
  id = row['id']
  title = row['title']
  #minute = row['minute']
  transcript = row['transcript']
  date = row['date']


  # For each search term, extract the relevant strings and add a row to the new DataFrame for each occurrence
  for term in search_terms.keys():
    extracted_strings = find_search_term(transcript, term)
    if extracted_strings:
      for extracted_string in extracted_strings:
        rows.append({'medium': medium,
                      'id': id, 
                      'title': title, 
                      #'minute': minute, 
                      'date': date, 
                      'search_term': term, 
                      'extracted_string': extracted_string})

# Create the new DataFrame from the list of rows
party_df = pd.DataFrame(rows, columns=['medium', 'id', 'title', 'minute', 'date', 'search_term', 'extracted_string'])