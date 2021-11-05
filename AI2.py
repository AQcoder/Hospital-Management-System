import pandas as pd
import nltk

df_raw = pd.read_csv('socialmedia-disaster-tweets-DFE.csv', encoding='ISO-8859-1')
df_raw.head(5)
df_text=df_raw['text'].copy()
sample_tweet=df_text.iloc[100]
tokenize_tweet=nltk.tokenize.word_tokenize(sample_tweet)
tokenize_raw=[nltk.tokenize.word_tokenize(x) for x in list(df_text)]
porter = nltk.stem.PorterStemmer()
wnl = nltk.stem.WordNetLemmatizer()

lemmed = [wnl.lemmatize(word) for word in tokenized_tweet]


stop = nltk.corpus.stopwords.words('english')
stop.append('@')
stop.append('#')
stop.append('http')
stop.append(':')

def process_tweet(tweet):
    tokenized_tweet = nltk.tokenize.word_tokenize(tweet)
    stemmed = [porter.stem(word) for word in tokenized_tweet]
    processed = [w.lower() for w in stemmed if w not in stop]
    return processed

def tokenizer(df):
    tweets = []
    for _, tweet in df.iterrows():
        tweets.append(process_tweet(tweet['text']))
    return tweets

tweets = tokenizer(df_raw)
