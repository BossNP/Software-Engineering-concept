# Import less key functions in custome package
import text_analyzer
from collections import Counter
import matplotlib.pyplot as plt

# Define Hyperparameters
N = 5

# Create variables
words1 = {'RT': 1, '@manideeplanka': 1, '@DataCamp': 1, 'this': 1, 'animation': 1, 'is': 1, 'as': 2,
          'beautiful': 1, 'and': 1, 'wonderful': 1, 'your': 1, 'courses': 1, 'are': 1}
words2 = {'New': 1, 'Tutorial': 1, 'Decorators': 1, 'in': 2, 'Python': 1, 'In': 1, 'this': 1, 'tutorial': 1,
          'learn': 1, 'how': 1, 'to': 1, 'implement': 1, '#decorators': 1, '#Python': 1}
words3 = {'RT': 1, '@drob': 1, 'We': 1, 're': 1, 'hiring': 1, 'an': 1, 'Instructor': 1, 'Recruiting': 1,
          'Intern': 1, 'at': 1, '@DataCamp': 1, 'great': 2, 'for': 1, 'someone': 1, 'enthusiastic': 1, 'about': 1,
          'DataCamp': 1, 'who': 1, 'wants': 1, 'to': 1, 'find': 1}
words4 = {'Read': 1, 'our': 1, 'new': 1, 'tutorial': 1, 'on': 1, 'Hacking': 1, 'Date': 1,
          'Functions': 1, 'in': 1, '#SQLite': 1}

file = open('data_tweet.txt', 'r', encoding='utf8')
data_tweets = file.readline()
file.close()


# Create a list of Counters
word_counts = [Counter(words1), Counter(words2), Counter(words3), Counter(words4)]

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

# Find and Plot the most N common words
top_items = word_count_totals.most_common(N)
text_analyzer.plot_counter(word_count_totals)


# create a new document instance from data_tweets
data_doc = text_analyzer.Document(data_tweets)

# print the first 5 tokens from data_doc
print(data_doc.tokens[:N])

# print the top 5 most used words in data_doc
print(data_doc.word_counts.most_common(N))


# Create a SocialMedia instance with data_tweets
dc_tweets = text_analyzer.SocialMedia(text=data_tweets)

# Print the top five most most mentioned users
print(dc_tweets.mention_counts.most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets.hashtag_counts)
