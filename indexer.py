import re
class ArabicCorpusIndexer:
    def __init__(self, corpus):
        self.corpus = corpus
        self.word_index = self._create_index()      
        
    def clean_text(self, text):
        # Remove emojis
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F700-\U0001F77F"  # alchemical symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                           u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           u"\U00002702-\U000027B0"  # Dingbats
                           u"\U000024C2-\U0001F251" 
                           "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)

        # Remove question marks and any other characters you don't want
        text = re.sub(r'[?]', '', text)

        return text

    def tokenize(self, text):
        cleaned_text = self.clean_text(text)
        
        return cleaned_text.split()
    

    def _create_index(self):
        unique_words = set()
        for sentence in self.corpus:
            words = self.tokenize(sentence)
            unique_words.update(words)
        
        # Assigning a unique index to each word
        return {word: index for index, word in enumerate(sorted(unique_words), start=1)}

    def get_index(self, word):
        # Returns the index of the word if it exists, otherwise None
        return self.word_index.get(word)

# # Example usage:
# corpus = [
#     "هذا نص عربي",
#     "هذا نص آخر",
#     "نص باللغة العربية"
# ]

# indexer = ArabicCorpusIndexer(corpus)
# print(indexer.get_index("نص"))  # Example to get the index of a specific word
# print(indexer.word_index)       # To see the entire word-index mapping
