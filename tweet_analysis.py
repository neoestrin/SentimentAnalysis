# -*- coding: utf-8 -*-
"""Tweet Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_xSx73FHUDVdJdVOz87GX36Vy2PYUzG-

# Sentiment Analysis

**Importing and Reading the dataset:**
"""

import pandas as pd

data = pd.read_excel("/content/drive/My Drive/Data/Misc/Tweets.xlsx")
data

"""**Deleting unneccessary columns and realigning the dataset:**"""

data.drop(["retweet_count", "tweet_coord", "tweet_created","tweet_location", "user_timezone"], axis = 1)
data = data[["tweet_id", "name", "airline", "text"]]
data

"""**Removing @VirginAmerica and @AmericanAir tags from the text bodies:**"""

data['text'] = data['text'].map(lambda x: x.strip("@VirginAmerica"))
data["text"].str.strip()
data

"""**Importing and Downloading Required Packages:**"""

import nltk
nltk.download("punkt")

from textblob import TextBlob

def process(senetence):
	blob = TextBlob(senetence)
	sum = 0
	p = 0
	n = 0
	for sentence in blob.sentences:
		if sentence.sentiment.polarity < 0 :
			n += 1
		elif sentence.sentiment.polarity > 0 :
			p += 1
	if n > p :
		return "Negative"
	elif n < p :
		return "Postive"
	else :
		return "Neutral"

for i in range(0,len(data)):
    data.loc[i, "sentiment"] = process(data["text"][i])

data

"""**Alternatively, we can also run a Lambda function to do the same thing:**"""

data["sentiment"] = data["text"].apply(lambda x: process(x))
data