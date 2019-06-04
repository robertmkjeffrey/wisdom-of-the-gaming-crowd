# COMP3770-Steam-Feature-Reviews

This project implements a feature-based summarisation algorithm, build for the purpose of summarising Steam reviews.

Project structure:

* `download_reviews/download_reviews.ipynb` - script used to download reviews from the Steam platform. This is a modified/re-implemented version of an existing tool; a link is provided within the script.
* `feature_mining/main.ipynb` - main script for feature summarisation. This work is original, with minor reference to github.com/esh-b/Feature-based-opinion-minin



## Installation & Set-up
Installation should be performed using Anaconda. Once Anaconda is running, create the environment:

```shell
conda env create -f environment.yml
```

Next, activate the environment:
```shell
conda activate COMP3770-Steam-Feature-Reviews
```

Finally, open jupyter notebook:
```shell
jupyter notebook
```