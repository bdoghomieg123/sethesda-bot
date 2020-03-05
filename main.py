import praw
import random as rando
import os
import time
import os.path
from common import clear


reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit("sethesda_submissions")

lines = open('replies.txt').read().splitlines()

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

while True:
    for submission in subreddit.new(limit=10):
        if submission.id not in posts_replied_to:
            if submission.link_flair_text == "Meme":
                reply = rando.choice(lines)
                print(reply)
                comment = submission.reply(reply)
                comment.mod.distinguish(sticky=True)
                print(f'Bot Repled to: "{submission.title}"')
                posts_replied_to.append(submission.id)


        with open("posts_replied_to.txt", "w") as f:
            for post_id in posts_replied_to:
                f.write(post_id + "\n")
