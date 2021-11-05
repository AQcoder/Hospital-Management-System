import nltk
import numpy as np
import random
import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')  # first-time use only tokenizer
nltk.download('wordnet')  # first-time use only Used for the lemmatizer

filepath = 'corona 2.txt'
corpus = open(filepath, 'r', errors='ignore')
raw_data = corpus.read()

x = raw_data.lower()

sent_tokens = nltk.sent_tokenize(x)


word_tokens = []
for i in sent_tokens:
    word_tokens += (nltk.word_tokenize(i))

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey", "hey there"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)



def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


response('what are chatbots')

flag = True
print("MATRIX: My name is Matrix. I will answer your queries about Covid-19 Virus. If you want to exit, type Bye!")
while (flag == True):
    user_response = input()
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("MATRIX: You are welcome..")
        else:
            if (greeting(user_response) != None):
                print("MATRIX: " + greeting(user_response))

            else:
                print("MATRIX: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("MATRIX: Bye! take care..")



