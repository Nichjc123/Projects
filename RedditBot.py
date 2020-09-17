#! /usr/bin/env python3
#This is a bot that is made to moderate subreddits
from vars import client_id, client_secret, username, password, user_agent
import praw

#Initialising the reddit bot using personal information
reddit = praw.Reddit(client_id = client_id,client_secret = client_secret, 
	username= username, password= password, user_agent = user_agent)

#Getting user input for the subreddit to moderate
usr_subreddit = input('Please indicate the subreddit you would like to moderate: ')
subreddit = reddit.subreddit(usr_subreddit)
keywords = ['this','is','a','list','of','curse','words']

#Going over new submissions in the subreddit stream
for submission in subreddit.stream.submissions():
	#Iterating over the comments in the posts
	submission.comments.replace_more(limit=0)

	for comment in submission.comments.list():
		#Creating a reply if any of the curse words are found
		if any(word in comment.body for word in keywords):
			comment.reply('Hey please watch your language')
		
