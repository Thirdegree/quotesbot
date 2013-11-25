import praw

r = praw.Reddit("Quotesbot v1.0 by /u/Thirdegree")

def login_():
	USERNAME = raw_input("Username\n>")
	PASSWORD = raw_input("Username\n>")
	r.login(USERNAME, PASSWORD)

trying = True
while trying:
	try:
		login_()
		trying = False
	except praw.errors.InvalidUserPass:
		print "Incorrect Username or Password"

def check_quotes(post_body):
	quotes = 0
	for i in post_body:
		if i == '"':
			quotes +=1
	return quotes%2

running = True
while running:
	comments = r.get_comments("thirdegree")
	for post in comments:
		if check_quotes(post.body):
			post.reply('"\nYou dropped this.')