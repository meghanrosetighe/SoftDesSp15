'''
read_tweets.py 
Reads saved tweets, calculates sentiment analysis and then plots them
'''

import json
from matplotlib import *
import matplotlib.pyplot as plt
import pandas as pd
import re
from pattern.en import *

def get_tweets(path):
	'''Here I will retrieve the list of tweets from the saved txt files and calculate sentiments'''
	tweets = []
	tweets_sents = []
	tweets_file = open(path, "r")

	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets.append(tweet['text'])
	    except:
	        continue

	for tweet in tweets:
		tweets_sents.append(sentiment(tweet))
	return tweets_sents

def plot_tweets(tweets, details, house):
	''' Here I will plot each tweet on a scale where the x value is sentiment polarity and the y value is subjectivity'''
	x_val = [x[0] for x in tweets]
	y_val = [x[1] for x in tweets]
	plt.plot(x_val,y_val, details, label = house)

if __name__ == '__main__':
	plt.figure()
	plt.hold(True)
	g_sents = get_tweets('gryffindor.txt')
	s_sents = get_tweets('slytherin.txt')
	r_sents = get_tweets('ravenclaw.txt')
	h_sents = get_tweets('hufflepuff.txt')
	plot_tweets(s_sents,'og','Slytherin')
	plot_tweets(g_sents,'or','Gryffindor')
	plot_tweets(h_sents,'oy','Hufflepuff')
	plot_tweets(r_sents,'ob','Ravenclaw')
	plt.xlabel('Positivity')
	plt.ylabel('Subjectivity')
	plt.title('Comparison of Four Hogwarts Houses')
	plt.legend()
	plt.show()
