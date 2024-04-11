import re
SOS_token = 0
EOS_token = 1

class Lang:
    def __init__(self):

        self.word2index = {}
        self.word2count = {}
        self.index2word = {0: "SOS", 1: "EOS"}
        self.n_words = 2  # Count SOS and EOS
        
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

    def addSentence(self, sentence):
        
        for word in sentence.split(' '):
            wrd = self.clean_text(word)
            self.addWord(wrd)
        
            
    def addWord(self, word):
        
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1
    
    
    def get_index2word(self):
        return self.index2word
    
    def get_word2index(self):
        return self.word2index
            

# corpus = [
#     "هذا نص عربي",
#     "هذا نص اخر",
#     "نص باللغة العربية"
# ]

# indexer = Lang()

# for sent in corpus:
#     indexer.addSentence(sent)
    
# print(indexer.word2index)
# print(indexer.index2word)
    
