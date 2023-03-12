import re
import pandas as pd

party_search_terms = {
  'die linke': 'linke',
  'linkspartei': 'linke',
  'die grünen': 'grüne',
  'spd': 'spd',
  'freien demokraten': 'fdp',
  'fdp': 'fdp',
  'cdu': 'cdu',
  'csu': 'csu',
  'alternative für deutschland': 'afd',
  'afd': 'afd', 
  'afg': 'afd'}


politician_df = pd.read_pickle('assets/bundestag.pkl')
politician_search_terms = politician_df.set_index('politician').to_dict()['party']


def find_search_term(transcript, search_term):
  # Use a regular expression to find all occurrences of the search term in the transcript
  pattern = r"(?i)\b" + re.escape(search_term) + r"\b"
  matches = re.finditer(pattern, transcript)

  # For each occurrence, extract a 21 word long string with the search term in the middle
  extracted_strings = []
  for match in matches:
    start_index = match.start()
    end_index = match.end()

    # Split the transcript into words
    words_before = transcript[:start_index].split()
    words_after = transcript[end_index:].split()
    if len(words_before) < 10:
      continue
    if len(words_after) < 10:
      continue

    # Extract the 21 word long string
    string = ' '.join(words_before[-10:] + [search_term] + words_after[:10])
    extracted_strings.append(string)

  return extracted_strings


def extract_search_terms(row, search_terms):
    # Create an empty list to store the rows of the new DataFrame
  rows = []

# Iterate over the rows of the original DataFrame
  medium = row['medium']
  id = row['id']
  title = row['title']
  minute = row['minute']
  transcript = row['transcript']
  date = row['date']


  # For each search term, extract the relevant strings and add a row to the new DataFrame for each occurrence
  for term in search_terms.keys():
    extracted_strings = find_search_term(transcript, term)
    if extracted_strings:
      for extracted_string in extracted_strings:
        rows.append(
          {'medium': medium,
          'id': id, 
          'title': title, 
          'minute': minute, 
          'date': date, 
          'search_term': term, 
          'extracted_string': extracted_string,
          'party': search_terms[term]})

  if not rows:
    return
  return rows
