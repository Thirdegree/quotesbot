import praw
from time import sleep
from collections import deque

r = praw.Reddit("Quotesbot v1.0 by /u/Thirdegree")
done = deque(maxlen=200)

def login_():
	USERNAME = raw_input("Username\n>")
	PASSWORD = raw_input("Username\n>")
	r.login(USERNAME, PASSWORD)
	return USERNAME

trying = True
while trying: # to login
	try:
		USERNAME = login_() # There's probably a more "right" way to do this, but I don't know it
		trying = False
	except praw.errors.InvalidUserPass:
		print "Incorrect Username or Password"

def check_quotes(post_body): # counts the number of quotes in the string
	quotes = 0
	for i in post_body:
		if i == '"':
			quotes +=1
	return quotes

running = True
while running:
	print "Next" #to show it's working
	comments = r.get_comments("thirdegree")
	for post in comments:
		quote_number = check_quotes(post.body)
		#not even number of quotes, not replying to itself, not already done
		if (quote_number%2) and (post.author.name!= USERNAME) and (not(post.id in done)):
			post.reply('"\nYou dropped this.')
			print "\"*%d"%quote_number # more to show it's working... I get nervous
			sleep(2)
		done.append(post.id)
	sleep(10)