from .token_utils import tokenize
from collections import Counter

# Define Document class
class Document:
    def __init__(self, text):
        self.text = text
        # Tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Perform word count with non-public count_words method
        self.word_counts = self._count_words()

    # non-public method to tally document's word counts with Counter
    # By defining methods as non-public you're signifying to the user that the method is only to be used inside the package.
    def _tokenize(self):
        return tokenize(self.text)

    def _count_words(self):
        return Counter(self.tokens)
