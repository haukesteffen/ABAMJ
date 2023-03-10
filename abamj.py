import argparse
import os
from src.scrape import scrape
from src.extract_mentions import extract_mentions
from src.classify_sentiment import classify_sentiment
from src.analyze_mentions import analyze_mentions
from src.analyze_sentiment import analyze_sentiment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--scrape", 
        help="scrape subtitle data from youtube channels",
        action="store_true")
    parser.add_argument(
        "-e",
        "--extract", 
        help="extract party and politician mentions from dataset",
        action="store_true")
    parser.add_argument(
        "-c",
        "--classify", 
        help="classify sentiment of extracted party mentions",
        action="store_true")
    parser.add_argument(
        "-a",
        "--analyze", 
        help="perform mention and sentiment analysis on extracted and classified mentions",
        action="store_true")
    args = parser.parse_args()

    if args.scrape:
        scrape()

    if args.extract_mentions:
        if os.path.isfile('data/minutewise.pkl'):
            extract_mentions()
        else:
            raise Exception('Please scrape subtitle dataset first.')

    if args.classify:
        if os.path.isfile('data/party_mentions.pkl') and os.path.isfile('data/politician_mentions.pkl'):
            classify_sentiment()
        else:
            raise Exception('Please extract party and politician mentions first.')
        
    if args.analyze:
        if os.path.isfile('data/party_sentiment_classifications.pkl') and os.path.isfile('data/politician_sentiment_classifications.pkl'):
            analyze_mentions()
            analyze_sentiment()
        else:
            raise Exception('Please classify sentiment of party and politician mentions first.')


if __name__ == "__main__":
    main()
