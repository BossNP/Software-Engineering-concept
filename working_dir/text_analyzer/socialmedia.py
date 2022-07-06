from .document import Document
from collections import Counter

def filter_word_counts(word_counts, first_char='#'):
    filter_word_counts = {}
    for words in word_counts:
        if words.startswith(first_char):
            filter_word_counts[words] = word_counts[words]
    return Counter(filter_word_counts)


class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')

    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')