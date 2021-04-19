import nltk
from spellchecker import SpellChecker
import random
import string #for python strings
print("What would you like to know about?\n( chatbot, cricket, tensorflow, python )")
topic = input(string)
if (topic!='chatbot'):
    spell=SpellChecker()
    misspelled=topic
    topic=spell.correction(topic)

f=open('C:/informationnltk/'+topic+'.txt','r',errors='ignore')
raw=f.read()
raw= raw.lower() #this is for converting everything to lowercase
sent_tokens=nltk.sent_tokenize(raw) #tokenizing sentences
word_tokens=nltk.word_tokenize(raw) #tokenizing words
lemmer = nltk.stem.WordNetLemmatizer()
#semantically-oriented dictionary of English included in NLTK.

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello","greetings!"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def retrieve_ngrams(sent_tokens):
    return [sent_tokens[i:i+2] for i in range (len(sent_tokens)-(2-1))]
def response(user_response):
    bot_response=''
    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx0 = vals.argsort()[0][-2]
    idx1=vals.argsort()[0][-3]
    idx2 = vals.argsort()[0][-4]
    idx3 = vals.argsort()[0][-5]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        bot_response=bot_response+"I am sorry! I don't understand you. Would you like to input the expected answer when you get it?(press n if no)"

        print(bot_response)
        resp=input()
        if resp=='n':
            return("okay")
        else:
         ans=input(string)
        with open('C:/informationnltk/'+topic+'.txt','a',errors='ignore') as myfile:
            myfile.write("\n \n"+ans)
        myfile.close()
        return("done")
    else:
        bot_response = bot_response+sent_tokens[idx0]+"\n"+sent_tokens[idx1]+"\n"+sent_tokens[idx2]+"\n"+sent_tokens[idx3]
        return bot_response

flag=True
print("WikiBOT: My name is WikiBOT. I will answer your queries about "+topic+". If you want to exit, type Bye!")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("WikiBOT: You are welcome.")
        else:
            if(greeting(user_response)!=None):
                print("WikiBOT: "+greeting(user_response))
            else:
                print("WikiBOT: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("WikiBOT: Bye! take care.")

