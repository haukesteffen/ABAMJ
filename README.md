# Introduction

This repository contains code for exploring automatic bias analysis in multimedia journalism. It creates a dataset from YouTube as well as ARD/ZDF Mediathek subtitle data and performs mention analysis and sentiment analysis ([Example #1](results/plots/mentions/party_mentions_zeromean.pdf), [Example #2](results/plots/sentiment/party_negative_zeromean.pdf)).

For details, please have a look at our paper Towards Automatic Bias Analysis in Multimedia Journalism (TODO). Citation information can be found at the bottom of this page.

```
ABAMJ
├──📂 assets
│   └── bundestag.pkl
├──📂 data
│   ├── mediathek_data.pkl
│   └── ...
├──📂 results
│   ├── 📂 dataframes
│   │    ├── 📂 mentions
│   │    │    └── ...
│   │    └── 📂 sentiment
│   │         └── ...
│   └── 📂 plots
│        ├── 📂 mentions
│        │    └── ...
│        └── 📂 sentiment
│             └── ...
├── LICENSE
├── .gitignore
├── README.md
├── setup.sh
└──📂 src
    ├── 📂 utils
    │    ├── __init__.py
    │    ├── scraper_util.py
    │    ├── extract_mentions_util.py
    │    ├── classify_sentiment_util.py
    │    ├── analyze_mentions_util.py
    │    └── analyze_sentiment_util.py
    ├── scraper.py
    ├── extract_mentions.py
    ├── classify_sentiment.py
    ├── analyze_mentions.py
    └── analyze_sentiment.py
```

## Setup
Make sure conda is installed on your system:
https://docs.conda.io/

```shell
git clone git@github.com:haukesteffen/ABAMJ.git
cd ABAMJ
conda env create -f env_abamj.yml
conda activate ABAMJ
```

## Pipeline

### 1. Scraper
```shell
python3 src/scraper.py
```

You may need to disable fork safety:
```shell
OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES python3 src/scraper.py
```
### 2. Mention Extraction
```shell
python3 src/extract_mentions.py
```

### 3. Sentiment Classification
```shell
python3 src/classify_sentiment.py
```

### 4. Mention Analysis
```shell
python3 src/analyze_mentions.py
```

### 5. Sentiment Analysis 
```shell
python3 src/analyze_sentiment.py
```

## Citation

TODO
