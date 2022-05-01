# Import the necessary modules

from nltk.tokenize import regexp_tokenize, TweetTokenizer
from NLP.src.nlp_utils import get_tweets_sample

tweets = get_tweets_sample()

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
re_tokenizer = regexp_tokenize(tweets[0], pattern1)
hashtags = re_tokenizer.tokenize()
print(hashtags)

# Write a pattern that matches both mentions (@) and hashtags
# pattern2 = r"(____)"
# # Use the pattern on the last tweet in the tweets list
# mentions_hashtags = ____
# print(___)

# # Use the TweetTokenizer to tokenize all tweets into one list
# tknzr = ___
# all_tokens = [__ for t in __]
# print(___)