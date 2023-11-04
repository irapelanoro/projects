#Build preprocessing pipeline

#Lowercasing: Makes all letters small for consistency.
#Removal of Emojis: Takes out any smiley faces or symbols.
#Removal of Punctuations: Gets rid of dots, commas, and other marks.
#Tokenization: Breaks the text into separate words.
#Stemming: Shortens words to their main form.
#Removal of Stop Words: Drops common unimportant words.


import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download necessary resources from NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Utility functions for preprocessing
def preprocess(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove emojis
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    
    # Initialize a Porter stemmer
    stemmer = PorterStemmer()
    
    # Stemming and remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    
    return tokens

