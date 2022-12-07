# Widsom of the Gaming Crowd
## Steam Feature Reviews

This project implements a feature-based summarisation algorithm, designed for summarisaing Steam reviews.

### Feature Summaries

Ever enjoyed a game that everyone else hates? 

One simple explanation is that different individuals value different aspects of a game to different extents. A shooter's lack of story might be a dealbreaker to one player; whereas another might only care about the gameplay.

This creates a challenge when summarising crowd-sourced reviews, such as on Steam. Providing a single number, e.g. "87% reccomended" misses the nuance of preference. To give extra context, we can provide ratings for each aspect. For example: 

Shooter Inc. <br/>
Total: 74% positive. <br/>
* Gameplay - 87% positive.
* Graphics - 61% positive.
* Story - 21% positive.

This project provides a baseline algorithm to generate these summarises from text reviews via topic extraction and sentiment analysis.

This work contributed to [The Wisdom of the Gaming Crowd (Robert Jeffrey, Pengze Bian, Fan Ji, and Penny Sweester, 2020)](https://dl.acm.org/doi/10.1145/3383668.3419915), submitted to CHI PLAY 2019. It was originally completed as part of the Individual Research Project course (COMP3770) at the Australian National University.

### Project structure:

* [`report.pdf`](report.pdf) - project report from original submission.
* [`download_reviews/download_reviews.ipynb`](download_reviews/download_reviews.ipynb) - download reviews from Steam.
* [`feature_mining/main.ipynb`](feature_mining/main.ipynb) - generate feature summaries from downloaded reviews.
* [`review_data.zip`](review_data.zip) (LFS) - review data used in original project report. Password is available upon request.

## Installation & Set-up
### Python
This project uses Python3. Instructions are provided for Anaconda setup below:

Create the environment:
```shell
conda env create -f environment.yml
```
Next, activate the environment:
```shell
conda activate steam-feature-reviews
```

Finally, open jupyter notebook:
```shell
jupyter notebook
```

### Generating Feature Summaries
First, identify the Steam `app_id` for the video game(s) of interest. This can be obtained from the URL of the Steam page. For example:

`https://store.steampowered.com/app/570/Dota_2/`<br/>
gives<br/>
`app_id = 570`

Secondly, use [`download_reviews.ipynb`](download_reviews/download_reviews.ipynb) to gather review data. >10k reviews (100 pages) are easily handled and makes a good starting point for analysis. More data can be easily gathered by running the script again due to the restart capabilities.

Finally, use [`feature_mining/main.ipynb`](feature_mining/main.ipynb) to summarise the reviews.

## Contributing

This repo is currently an archive, so new features will not be added. 
However, forks are welcome! 
