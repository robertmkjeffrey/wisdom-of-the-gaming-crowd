import pandas as pd # Managing dataframes
from tqdm.auto import tqdm # Progress bars. Will automatically choose between GUI & console bars.

import nltk # NLP

def preprocess(df, lower_case=False, minimum_length=0):
    """Preprocess a dataframe of reviews into a series of sentence tokens.
    Parameters:
    -----------
    
    df: pd.Dataframe
        dataframe of reviews
    lower_case: bool, optional
        if reviews should be converted to lower case
    minimum_length: int, optional
        minimum number of review tokens required to keep the review.
        
        
    Returns:
    --------
    pd.Series(list(list(str)))
        Series of reviews, each review being tokenised into a list of sentences, composed of lists of word tokens.
    """
    
    def tokenize_review(review):
        """Sentence tokenise a single review."""
        
        if(lower_case):
            review = review.lower()
        
        sentences = nltk.tokenize.sent_tokenize(review)
        
        token_count = 0
        
        sentence_tokens = []
        for sentence in sentences:
            tokens = nltk.tokenize.word_tokenize(sentence)
            token_count += len(tokens) # Add the number of tokens in the sentence to the total tokens
            sentence_tokens.append(tokens)
            
        # If the review has enough tokens, return them. Otherwise, return None.
        if(token_count >= minimum_length):
            return sentence_tokens

    # Choose the reviews to use
    reviews = df['review']
    
    # Tokenise reviews
    tqdm.pandas() # progress bar
    preprocessed_reivews = reviews.progress_apply(tokenize_review)
    preprocessed_reivews.dropna(inplace=True)
    return preprocessed_reivews