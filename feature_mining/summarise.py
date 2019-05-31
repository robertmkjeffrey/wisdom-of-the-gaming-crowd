import pandas as pd # Managing dataframes
from tqdm.auto import tqdm # Progress bars. Will automatically choose between GUI & console bars.

import re # Regex expressions

import nltk # NLP
from nltk.sentiment.vader import SentimentIntensityAnalyzer # Sentiment analyser

from collections import defaultdict

def summarise(reviews):
    """Create a feature summary for a series of reviews.
    
    Parameters:
    -----------
    reviews: pd.Series(list(list(str)))
        Series of reviews, each review being tokenised into a list of sentences, composed of lists of word tokens.
        
    Returns:
    --------
    features: {string : (int, int, int)}
        dictionary of features extracted from reviews. 
        The value for each feature is (total_noun_score, positive_score, negative_score)."""
    
    # Dictionaries for our features and their scores. Default score is 0.
    noun_positive_score = defaultdict(int)
    noun_negative_score = defaultdict(int)
    noun_adjective_count = defaultdict(int)
    
    # Manually derived set of words that show up commonly as features, but don't provide information to readers.
    stopword_features = set( 
        ["game"
        ,"games"
        ,"i"
        ,"thing"
        ,"things"
        ,"stuff"
        ,"fun"
        ,"way"
        ,"edition"
        ,"play"
        ,"review"
        ,"☐"
    ])
    
    # Ascii characters that should not be part of a token
    invalid_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    
    
    def find_nearest_noun(line, index):
        """Find the nearest noun to the current index. 
        
        If two nouns are the same distance away, choose the one in front."""
        
        offset = 1
        # While within line bounds:
        while (index+offset) < len(line) or (index-offset) > -1:
            # If the token at index + offset is a noun, return it
            if (index+offset) < len(line) and line[index+offset][1][:2] == "NN":
                return line[index+offset][0]
            # If the token at index - offset is a noun, return it
            elif (index-offset) > -1 and line[index-offset][1][:2] == "NN":
                return line[index-offset][0]
            # Otherwise increment the counter
            offset += 1
        return None

    def get_context(line, index, nearest_noun):
        """Get the context of a adjective noun combo.
        
        Computed by getting the current adjective, the two tokens before (if they exist), and the nearest noun."""
        
        context_list = []
        if index >= 2:
            context_list.append(line[index-2][0])
        if index >= 1:
            context_list.append(line[index-1][0])

        context_list.append(line[index][0])
        context_list.append(nearest_noun[0])

        return " ".join(context_list)
    
    
    # Define our sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    
    # For each review, score the nouns.
    for review in tqdm(reviews):        
        tokens = nltk.pos_tag_sents(review)
        #tokens = stem_review(tokens)

        for line in tokens:
            for index, token in enumerate(line):
                # If the token's tag doesn't start with "JJ" (adjective), skip it
                if token[1][:2] != "JJ":
                    continue
                # Find nearest noun and add 1 to the noun score
                nearest_noun = find_nearest_noun(line, index)
                # If there's not a nearest noun, continue
                if nearest_noun is None:
                    continue

                # If the nearest noun is a stopword, continue
                if nearest_noun in stopword_features:
                    continue
                    
                # If the nearest noun has an invalid character, continue
                if invalid_characters.search(nearest_noun) is not None:
                    continue
                
                # Add to the count for the nearest noun
                noun_adjective_count[nearest_noun] += 1

                # Get the context for sentiment analysis
                context = get_context(line, index, nearest_noun)
                
                # Analyse the sentiment of the noun, and add to the counters
                sentiment = sid.polarity_scores(context)

                if sentiment['compound'] > 0:
                    noun_positive_score[nearest_noun] += 1
                elif sentiment['compound'] < 0:
                    noun_negative_score[nearest_noun] += 1
                    
    return noun_adjective_count, noun_positive_score, noun_negative_score
    