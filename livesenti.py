import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re

def calctime(a):
	return time.time()-a
#we count time by subtracting the current time - starting time 
positive=0
negative=0
compound=0

count=0
initime=time.time()
plt.ion()

import rough

ckey=rough.ckey
csecret=rough.csecret
atoken=rough.atoken
asecret=rough.asecret

"""whenever on_data gets the data it gets it in the form of json, we import json and read json file,we have to decode the json file to get our data 
tweet is present as matrix in all_data, here tweet is present as [text] plus the tweet is very dirty contains emojis etc so to refine it we use re.findal and get all the text """
class listener(StreamListener):
	def on_data(self,data):
		global initime
		t=int(calctime(intime)) #round off the time to integer
		all_data=json.loads(data)
		tweet=all_data["text"].encode("utf-8")
		tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
		blob=TextBlob(tweet.strip()) #used for sentiment analysis and pass the tweet and we get a textblob variable which we use for sentiment analysis

		global positive
		global negative
		global compound
		global count

		count=count+1
		senti=0 #because tweet might have two sentences and texyblob calculates the sentiments for each sentence
		for sen in blob.sentences:
			senti=senti+sen.sentiment.polarity
			if sen.sentiment.polarity >= 0:
				positive=positive+sen.sentiment.polarity
			else:
				negative=negative+sen.sentiment.polarity

		compound=compound+senti
		print count
		print tweet.strip()
		print senti
		print t
		print str(positive) + ' ' + str(negative) + ' ' + str(compound)



		plt.axis([ 0, 70, -20,20])
		plt.xlabel('Time')
		plt.ylabel('Sentiment')
		plt.plot([t],[positive],'go',[t] ,[negative],'ro',[t],[compound],'bo')
		plt.show()
		plt.pause(0.0001)
		if count==200:
			return False
		else:
			 return True

			    def on_error(self,status):
			    	print status



auth=OAuthHandler(ckey,csecret) #we are authorising ourselves
auth.set_access_token(atoken,asecret)

twitterStream= Stream(auth, listener(count)) #here count is some variable and check for count if equal to given value we stop 
twitterStream.filter(track=["Narendra Modi"])
