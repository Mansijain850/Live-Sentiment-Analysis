from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'TbtXEHu7c7MLF5mLwtlVuzZWs'
csecret = 'gpJkew4H7GrVOm7mepMI9nQ4j6JTBwZEoGn227lPzp65mrGALZ' 
atoken = '862342851199328257-EqKAMbIDT3dWiGZp3lfrdTMkMklCVEr'
asecret = 'cNi6DPGlCHPddHNR9NLDn0eBuT8sxSTnvio6arsYkeSWw'


"""class Listener(StreamListener):
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["car"])
"""

		