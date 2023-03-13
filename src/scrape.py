#!/usr/bin/env python

from src.utils.scrape_util import channels, get_raw_df, get_minutewise_df
import pandas as pd
from pandarallel import pandarallel


def scrape():
    pandarallel.initialize(progress_bar=True)
    data_df = pd.DataFrame()
    i = 0
    for channel, id in channels.items():
        i += 1
        print(f"\n\nScraping subtitles and metadata of channel: {channel}... ({i}/{len(channels)})")
        raw_df = get_raw_df(channel, id)
        data_df = pd.concat([data_df, raw_df], axis=0)
    data_df.reset_index(inplace=True)
    data_df.to_pickle('data/data.pkl')

    minutewise_df = get_minutewise_df(data_df)
    minutewise_df.to_pickle('data/minutewise.pkl')


if __name__ == "__main__":
    scrape()
