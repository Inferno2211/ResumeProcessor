import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

import spacy
print(spacy.__version__)

stop_words = stopwords.words('english')
print(stop_words[:10])