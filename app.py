import praw
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

# Create an authorized Reddit instance.
reddit = praw.Reddit(client_id=config["config"]["client_id"],
                     client_secret=config["config"]["client_secret"],
                     user_agent=config["config"]["user_agent"],
                     username=config["config"]["username"],
                     password=config["config"]["password"]
)

# Obtain subreddit instance.
subreddit = reddit.subreddit(config["config"]["subreddit"])

words = configparser.ConfigParser()
words.read("words.ini")

for submission in subreddit.new(limit=3):
    # Sort the subreddit submissions by new.
    submission.comment_sort = "best"
    submission.comments.replace_more(limit=0)
    # Get the comment from the iteration.
    for comment in submission.comments:

        # Checks if the comment doesn't already have a reply.
        if comment.replies.__len__() == 0:
        
            # Iterate through the words.ini.
            for words_key in words["words"]:

                # Compare if the comment body contains a misspelled word.
                comment_string = comment.body.lower()
                if words_key in comment_string:
                    comment.reply(words_key + " is spelled wrong. The correct way is " + words["words"][words_key] + ".")