from TweepyAPI_Extended import tweet_list
import preprocessor as p
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stems = []

dataset=[]
tweets=[]
stop_words = set(stopwords.words('english'))

for tweet in tweet_list:
    tweet=p.tokenize(tweet)     
    
for tweet in tweet_list:
    p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.HASHTAG,p.OPT.RESERVED,p.OPT.NUMBER,p.OPT.EMOJI)
    dataset.append(p.clean(tweet))   
    
    
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for tweet in dataset:
    tweet=tweet.lower()
    # Removing punctuations in string, Using loop + punctuation string 
    for ele in tweet:  
        if ele in punc:  
            tweet = tweet.replace(ele,"")
    words=tweet.split(" ")
    filtered_sentence = "" 
    for w in words: 
        w=porter.stem(w)
        if w not in stop_words and len(w)>1:  
            filtered_sentence+=w
            filtered_sentence+=" "
    tweets.append(filtered_sentence)
    
for tweet in tweets:
    print(tweet)
    print("------------------------")

