from utils.scraper_util import *

data_df = pd.DataFrame()
for name, id in channels.items():
    raw_df = get_raw_df(id)
    minutewise_df = get_minutewise_df(raw_df)
    data_df = pd.concat([data_df, minutewise_df], axis=0)
data_df.to_pickle('../data/data.pkl')