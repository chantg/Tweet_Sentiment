import pandas as pd
import numpy as np
import nltk 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 


from sklearn.naive_bayes import MultinomialNB
import re

def removeLinks(line):
    newLine = re.sub("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"," ",line)
    return newLine

def tokenize(fn):
    tokens = []
    fn  = removeLinks(fn)
    words = re.split('[^a-z0-9]+', fn.lower())
    for word in words:
    	if len(word) > 2:
        	tokens.append(word)
    return tokens

def getStringArrayFromNumpyDataFrame(dataframe):
    list=[]
    for s in dataframe.values:
        if len(str(s[0]))>0:
            list.append(str(s[0]))
    return list

def getEmotions(text,clf):

	text = tokenize(text)
	#print(text)
	X_new_counts = count_vect.transform(text)
	X_new_tfidf = tfidf_transformer.transform(X_new_counts)
	predicted = clf.predict(X_new_tfidf)

	positive_count = 0
	for x in predicted:
		if x==1:
			positive_count=positive_count+1
	return positive_count;


def getEmotionFromText(text):
    positives=getEmotions(text,clf_positive)
    negatives=getEmotions(text,clf_negative)
    bad=getEmotions(text,clf_bad)

    print(positives, negatives, bad)

    if(bad>0):
        return("Bad tweet ->%s"%(text))
    else:
        if(positives-negatives)>0:
            return("Positive tweet ->%s"%(text))
        elif(negatives-positives)>0:
            return("Negative tweet ->%s"%(text))
        else:
            return("Neutral tweet ->%s"%(text))



train_data_csv_name="half.txt"


df_x_words = np.genfromtxt(train_data_csv_name, delimiter=',', usecols=(0), dtype=str)
df_y_positive= np.genfromtxt(train_data_csv_name, delimiter=',', usecols=(1))
df_y_negative= np.genfromtxt(train_data_csv_name, delimiter=',', usecols=(2))
df_y_bad = np.genfromtxt(train_data_csv_name, delimiter=',', usecols=(3))

print(df_x_words)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(df_x_words)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


clf_positive = MultinomialNB().fit(X_train_tfidf, df_y_positive)
clf_negative = MultinomialNB().fit(X_train_tfidf, df_y_negative)
clf_bad = MultinomialNB().fit(X_train_tfidf, df_y_bad)


outputfile = open('sentimentanalysis.txt','w')

tweet_file_name="tweets_UCI.txt"
with open(tweet_file_name, encoding='latin-1') as f:
	for line in f:
		tmpstr = getEmotionFromText(line)
		print(tmpstr)
		outputfile.write(tmpstr)

        
outputfile.close()
